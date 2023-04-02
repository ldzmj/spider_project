import urllib.request

url = "http://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
# 代理ip
proxies = {
    "http": "121.13.252.61:41564"
}
request = urllib.request.Request(url=url, headers=headers)
# 固定三句话
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

info = response.read().decode("utf-8")
with open("ip.html", "w", encoding='utf-8')as fp:
    fp.write(info)