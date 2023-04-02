import requests
import json
# 百度翻译
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Cookie": 'BIDUPSID=06268C5CD00B46B87AE9A5E001FDD461; PSTM=1604675212; __yjs_duid=1_9134255161280f1c992654bb9afdb7b71619183144353; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=9C6BAE4592CE85C121DB959F2960CDAA:FG=1; APPGUIDE_10_0_2=1; newlogin=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=9C6BAE4592CE85C121DB959F2960CDAA:FG=1; BA_HECTOR=2g8004a0048124a1258180ck1i1b7gn1n; ZFY=m2SDwIn2Zitwu5WVLJtZNbbydQMTdMcZjg2UuFGInGY:C; RT="z=1&dm=baidu.com&si=628de4be-ece7-4258-8191-17f70342203a&ss=lfe7w304&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=29w&ul=7qoc&hd=7qtc"; H_PS_PSSID=36545_38412_38113_38124_38364_38401_37861_38171_38289_38237_37921_38316_38285_26350_22158_37881; delPer=0; PSINO=5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677926891,1678124399,1679042229,1679222346; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1679222359; ab_sr=1.0.1_ZTViMDRkN2NjMWMyNWExNzM1Mjc4ZGZiZWE5ODExNGMxMmYxZTg3MDdlZDNlMjg4MzhhNDI0ZDNiNmIwNDdiMGVhNDQ1NDQ1N2RlYzliYTRlNDA4ZjcxZmIzYzgwNGEwMTdhNjkyODUzMzhlZWI0NWI3YTc2ODA4ZjQ3N2IxMmYwMThhYzlmZGI2YjQ1ZGQ0Mzk5YzZhYWVmYmJlYjQ1OA=='
}
data = {
    "kw": "eye"
}
response = requests.post(url=url, data=data, headers=headers)
context = response.text
js = json.loads(context, encoding='utf-8')
# print(js['data'])
for item in js['data']:
    print(item['k'], item['v'])
