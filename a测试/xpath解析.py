from lxml import etree
import urllib.request

'''
url = "https://movie.douban.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    'Cookie': 'douban-fav-remind=1; bid=UuuNwd3FfgE; __yadk_uid=JlXvwnKXSdCXMIDf2ZAqPnI87JJpZsTA; __gads=ID=05f848a71be3b908-22cbcf0023da00fc:T=1677240652:RT=1677240652:S=ALNI_MZrE_rradMAOPq7W_CVU2RSxoZGYQ; ll="118197"; _vwo_uuid_v2=D0E05F4230930BF842E861392EAB1439B|b0565fdecee432f021e2be20d591ad51; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1677820991; __gpi=UID=00000bcb773974be:T=1677240652:RT=1678521848:S=ALNI_MZOMFyPSAHOkT9yq1X5NBQQZAtqow; __utmz=30149280.1678972185.17.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1678972185.17.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1679036579%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2BNLCvcUCfB5AaOSntc1jRa6kr6uugb-nK9T6b7ui9atDfbCnK1cbtmM3vP2VQEN%26wd%3D%26eqid%3Dc5bf00a50001bdfe0000000464131515%22%5D; _pk_id.100001.4cf6=8c9121af373af442.1677240651.19.1679036579.1678985003.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1611782961.1677240651.1678984883.1679036579.19; __utmb=30149280.0.10.1679036579; __utmc=30149280; __utma=223695111.413038286.1677240651.1678984883.1679036579.19; __utmb=223695111.0.10.1679036579; __utmc=223695111'}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
with open("douban.html", "w", encoding='utf-8')as fp:
    fp.write(html)
'''
# 解析本地文件用etree.parse()
# 解析服务器文件用etree.HTML()
# tree=etree.HTML()
tree = etree.parse("xpath解析.html")
# xpath解析的数据是列表类型的
# 查找所有有li属性的标签,text()查看标签内容
label = tree.xpath('//ul/li/text()')
# 查找li标签中有id属性的标签，'//li/@id'显示id值，//li[@id]显示标签
label = tree.xpath('//li[@id]/text()')
# 查找id为home的li标签
label = tree.xpath('//li[@id="home"]/text()')

print(label)
print(len(label))
