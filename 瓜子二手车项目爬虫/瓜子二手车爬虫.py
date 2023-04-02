import requests
import json
import openpyxl

# 加密数字
number_dict = {
    '&#59854;': '0',
    '&#58397;': '1',  # 1
    '&#58928;': '2',  # 2
    '&#60146;': '3',  # 3
    '&#58149;': '4',  # 4
    '&#59537;': '5',  # 5
    '&#60492;': '6',  # 6
    '&#57808;': '7',  # 7
    '&#59246;': '8',  # 8
    '&#58670;': '9',  # 9
}

wb = openpyxl.Workbook()
ws = wb.active  # 获取工作表
ws.title = '汽车总数据表'
ws.append(['汽车名称', '上牌时间', '公里数', '首付', '总价'])

# for i in range(1, 81):
url = 'https://mapi.guazi.com/car-source/carList/pcList?versionId=0.0.0.0&sourceFrom=wap&deviceId=11418f4c-72d7-4013-a9c2-e0e8f3dc0c8c&osv=Windows+10&page=1&pageSize=20&city_filter=123&city=123&guazi_city=123&platfromSource=wap'
headers = {
    'cookie': 'uuid=11418f4c-72d7-4013-a9c2-e0e8f3dc0c8c; sessionid=688feb3a-ffd9-4e47-f54b-e4830be12e75; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; tktrackid=531533323807703041; user_city_id=-1; cityDomain=www; puuid=4cc51312-ebd6-49fb-85f2-70c4aa0b7979; cainfo=%7B%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%2211418f4c-72d7-4013-a9c2-e0e8f3dc0c8c%22%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
response.encoding = 'UTF-8'
info = response.text
# print(info)
# print(type(info))
data = json.loads(info)
print(data)
# print(type(data))
car_list = data['data']['postList']
# print(car_list)
# print(type(car_list))

for car in car_list:
    car_brand = car['title']  # 车辆名称
    license_date = car['license_date']  # 上牌时间
    road_haul = car['road_haul']  # 公里数
    first_pay = car['first_pay']  # 首付
    price = car['price']  # 总价

    print("汽车名称:" + car_brand)
    # print(type(car_brand))

    print("上牌时间:" + license_date)
    # print(type(license_date))

    road_str = road_haul.split('.')
    print(road_str)
    # print(type(road_str))
    # 提取整数
    if len(road_str[0]) <= 8:
        a = road_str[0]
        b = ''
        # print(number_dict[a])
    elif len(road_str[0]) <= 16:
        a = road_str[0][:8]
        b = road_str[0][8:]
        # print(number_dict[a])
        # print(number_dict[b])
    # 提取小数
    if len(road_str) == 1:
        c = road_str[1][:8]
        # d = road_str[1][8:]
    # print(number_dict[c])
    # print(type(d))
    # print(d)
    # print(type(c))
    if b != '':
        landmark_str = number_dict[a] + number_dict[b] + "." + number_dict[c]
    else:
        landmark_str = number_dict[a] + "." + number_dict[c]
    # print(type(landmark_str))
    print("公里数:" + landmark_str)  # 打印公里数
    # print(type(road_haul))

    print("首付:" + first_pay)
    # print(type(first_pay))

    print("总价:" + price)
    # print(type(price))

    print('----------------------------------------------------')
