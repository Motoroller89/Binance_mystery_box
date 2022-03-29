import random
import threading
import time
from datetime import datetime, timedelta

import requests

#from binance1.settings import headers

from create_bot import db




def event_is_not_over(status: int) -> bool:
    return status == 0

def headers_is_right(id) -> bool:
    date =db.post_date_in_setting(id)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'clienttype': 'web',
        'cookie': date[1].encode('UTF-8'),
        'csrftoken': date[0],
        'content-type': 'application/json',
        'bnc-uuid': date[3],
        'device-info': date[2],

    }
    user_info = 'https://www.binance.com/bapi/accounts/v1/private/account/user/base-detail'
    response = requests.post(user_info, headers=headers)

    if response.status_code == 200:
        print('Successfully connected\n')
        return True
    else:
        print('Something wrong...')
        print('Check please: COOKIE, CSRFTOKEN, headers')
        return False

def get_random_proxy():
    with open('proxies.txt', 'r') as file:
        proxies = [proxy.replace('\n', '') for proxy in file.readlines()]

    return random.choice(proxies)

def send_requests_to_buy(box, start_sale_time: datetime):
    threads = list()
    d = True
    while  d:
        current_time = datetime.today()
        #if start_sale_time <= (current_time - timedelta(seconds=0.1)):
        for _ in range(1, 100):
            request = threading.Thread(
                target=box._buy_box,
                args=(get_random_proxy(),)
            )
            request.start()
            threads.append(request)
            time.sleep(0.07)

        for thread in threads:
            thread.join()

        d = False
