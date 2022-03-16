CSRFTOKEN = '3bdbcffc814d1141da807b131f9c0465'
COOKIE = 'cid=jaHbJQAq; nft-init-compliance=true; _ga=GA1.2.919063373.1638895974; bnc-uuid=0c467b66-a0da-4b7a-9f5c-cc9927891927; source=referral; campaign=www.binance.com; theme=light; _gcl_au=1.1.2126045311.1644587156; BNC_FV_KEY=3204c6c2811dab928daaf65e8430349fed91d249; fiat-prefer-currency=RUB; userPreferredCurrency=RUB_USD; home-ui-ab=A; se_gd=BgBE1Q1ETAJUhRQ4KGhIgZZEgUxcSBVV1sCJbUUdldQUgWlNXVxX1; se_gsd=BikkBSBmJSg0UCc3J1UyIAQnG1cPBgMBUlxFUlFRV1dWDVNS1; _gid=GA1.2.737160585.1646928161; __ssid=1c032f6234e857b1798ddf06d2a6b7d; rskxRunCookie=0; rCookie=xdltr24pvpmo2ieooux3enl0qwwxax; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22319662668%22%2C%22first_id%22%3A%2217d95e419518f4-0998bb93536edc-978183a-2073600-17d95e41952aa3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d95e419518f4-0998bb93536edc-978183a-2073600-17d95e41952aa3%22%7D; monitor-uuid=dd932870-d26e-4770-9ff7-34e5998ff7ac; BNC_FV_KEY_EXPIRE=1647452066896; se_sd=lAQVhUgUbEAUAwFpXEBEgZZAwHhpREVV1sTJQW0RlZXVQC1NXV1S1; gtId=2d4587bd-eff0-454f-b335-be178995b675; s9r1=BE88F0287C1548673396837BFA99965F; cr00=2B812F79689E7F0242224FCF8C57BF54; d1og=web.319662668.6F14E0D573B1A8416B23A5BE5F449595; r2o1=web.319662668.D2EC71D682EDD647B24B22EF512BB440; f30l=web.319662668.E7854174D85911C839B79394B3D546B1; logined=y; __BINANCE_USER_DEVICE_ID__={"57af461d7bef578d8dc49a07ae77621c":{"date":1647274706260,"value":"1647274706862yGh4hsOtXOxxgnuwQT5"},"f7961cc02a29e1eac591578b3035f385":{"date":1647365923510,"value":"1647365923916efJ2s7rlyiSfeGDHkYo"},"0f683b6ec4b84df55ee0b4f2c5c2fe54":{"date":1642931887835,"value":"1642931887427HIhd5sHo5EygLztIsLS"},"e6ecd8056055640a9a314d7c24fd4060":{"date":1646561095545,"value":"1646561096222342z9EHPVRYfvzl3tMX"}}; p20t=web.319662668.5566F9CDC4B1E2F3EC1D48E3459F3267; FA5540=2; pl-id=319662668; lastRskxRun=1647366159452; lang=ru; _gat_UA-162512367-1=1; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Mar+15+2022+20%3A55%3A59+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=2c8a242c-01f2-4283-8a6f-3c21484b63c8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false'


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'clienttype': 'web',
    'cookie': COOKIE.encode('UTF-8'),
    'csrftoken': CSRFTOKEN ,
    'content-type': 'application/json',
    'bnc-uuid': '1',#bnc_uuid,
    'device-info': '1' #device_info,

}


#def register_handlers_data1(dp: Dispatcher):
#    dp.register_message_handler(gop,Text(equals="Upload"))

