import requests
import json

'''
数据获取模块：
https://mapi.guazi.com/car-source/carList/pcList?versionId=0.0.0.0&
sourceFrom=wap&deviceId=bf067bbf-1398-4127-8b52-49203c124cc0&osv=Windows+10&minor=&sourceType=&
ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&
gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&
fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&
monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&
page=80&pageSize=20&city_filter=123&city=123&guazi_city=123&platfromSource=wap
'''

url = 'https://mapi.guazi.com/car-source/carList/pcList?versionId=0.0.0.0&sourceFrom=wap&deviceId=bf067bbf-1398-4127-8b52-49203c124cc0&osv=Windows+10&minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page=1&pageSize=20&city_filter=123&city=123&guazi_city=123&platfromSource=wap'
headers = {
    'cookie': 'uuid=bf067bbf-1398-4127-8b52-49203c124cc0; cainfo=%7B%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22bf067bbf-1398-4127-8b52-49203c124cc0%22%7D; user_city_id=-1; cityDomain=www; sessionid=1bfd908e-426b-4b0f-e1b2-4f4d34887255; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'UTF-8'
info = response.text
# print(type(info))
# 将字符串转成json格式
data = json.loads(info)
print(data)
print(type(data))
