number_dict = {
    '&#59854;': '0',
    '&#58397;': '1',
    '&#58670;': '2',
    '&#58928;': '3',
    '&#60492;': '4',
    '&#59246;': '5',
    '&#57808;': '6',
    '&#60146;': '7',
    '&#59537;': '8',
    '&#58149;': '9'
}
print(number_dict['&#58149;'])
# road_haul = car['road_haul']  # 公里数
# # road_str = road_haul.split('.')
# print(road_str)
# # print(type(road_str))
# # 提取整数
# if len(road_str[0]) <= 8:
#     a = road_str[0]
#     b = ''
#     # print(number_dict[a])
# elif len(road_str[0]) <= 16:
#     a = road_str[0][:8]
#     b = road_str[0][8:]
#     # print(number_dict[a])
#     # print(number_dict[b])
# # 提取小数
# if len(road_str) == 1:
# # c =
# c = road_str[1][:8]
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
