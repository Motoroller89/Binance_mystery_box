import json
from abc import abstractmethod
from collections import defaultdict
from datetime import datetime
from typing import Optional, Union

import requests

from binance1.handlers import event_is_not_over
from binance1.schemas import Body, Headers
#from binance1.settings import headers
from create_bot import db

class BaseBox:

    def __init__(self):
        self._box_list = 'https://www.binance.com/bapi/nft/v1/public/nft/mystery-box/list?page=1&size=15'

    def get_list_boxes(self) -> dict:
        return requests.get(self._box_list).json()['data']

    def get_avalible_boxes(self) -> dict:
        avalible_boxes = defaultdict(dict)
        boxes = self.get_list_boxes()
        box_num = 0

        for box in boxes:
            status = box['status']
            name = box['name']
            product_id = box['productId']

            if event_is_not_over(status):
                box_num += 1
                avalible_boxes[str(box_num)] = {
                    'name': name,
                    'product_id': product_id
                }

        return avalible_boxes

    @staticmethod
    def log_info_boxes(avalible_boxes: dict) -> None:
        for box_num, value in avalible_boxes.items():
            print(f'{box_num}. {value["name"]}')



class Box(BaseBox):

    def __init__(
        self,
        amount: int=0,
        product_id: Optional[Union[str, int]]='',
        id: int=0,

    ):
        super().__init__()
        self._box_info: str = 'https://www.binance.com/bapi/nft/v1/friendly/nft/mystery-box/detail?productId='
        self._box_buy: str = 'https://www.binance.com/bapi/nft/v1/private/nft/mystery-box/purchase'

        self._product_id = product_id
        self._amount = amount

        date = db.post_date_in_setting(id)
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'clienttype': 'web',
            'cookie': date[1].encode('UTF-8'),
            'csrftoken': date[0],
            'content-type': 'application/json',
            'bnc-uuid': date[3],
            'device-info': date[2],

        }
        self._headers: Headers = headers

        self._body: Body = {
            'productId': product_id,
            'number': amount
        }


    @property
    @abstractmethod
    def _get_box_info(self) -> dict():
        return requests.get(self._box_info + str(self._product_id)).json()['data']

    @property
    @abstractmethod
    def _get_start_sale_time(self) -> datetime:
        start_sale = self._get_box_info['startTime']
        start_sale_time = datetime.fromtimestamp(start_sale/1000)
        return start_sale_time

    @abstractmethod
    async def _buy_box(self, proxy) -> json:
        response = await requests.post(
            self._box_buy, headers=self._headers,
            data=json.dumps(self._body),
            proxies={'http': f'http://{proxy}/'}
        )
        print(response.json())
        return response


box_info = BaseBox()
avalible_boxes = box_info.get_avalible_boxes()