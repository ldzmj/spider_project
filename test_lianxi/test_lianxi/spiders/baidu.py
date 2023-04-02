import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，爬虫的时候使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["http://www.baidu.com"]
    # 起始的url地址，指第一次要访问的域名，自动添加了http协议
    start_urls = ["http://www.baidu.com/"]

    # 执行了start_urls之后执行的方法，方法中的response就是返回的对象
    # 相当于response=urllib.request.urlopen()或requests.get()
    def parse(self, response):
        print("爬取完毕！！！")
