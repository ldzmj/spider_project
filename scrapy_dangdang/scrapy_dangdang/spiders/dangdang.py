import scrapy

from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    # 如果是多页下载的话，那么必须要调整allowed_domains的范围，一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = "http://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        print(f"==============第{self.page}页=================")
        # 书名name=//ul[@id="component_59"]/li/a/@title
        # 链接link=//ul[@id="component_59"]/li/a/@href
        # 图片photo=//ul[@id="component_59"]/li/a/img/@src
        # 图片采用懒加载，第一张图片是正常的，后面的就是把@src换成@data-original
        # 价格price=//ul[@id="component_59"]/li/p[@class="price"]/span[1]/text()
        # 详情detail=//ul[@id="component_59"]/li/p[2]/text()
        # 以上所有的都共享li标签
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            name = li.xpath('./a/@title').extract_first()  # 书名
            link = li.xpath('./a/@href').extract_first()  # 链接
            photo = li.xpath('./a/img/@data-original').extract_first()  # 图片
            # 第一张图片不是懒加载，没有data-original，它的src就是图片链接
            if photo is None:
                photo = li.xpath('./a/img/@src').extract_first()
            else:
                photo = photo
            price = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()  # 价格
            detail = li.xpath('./p[2]/text()').extract_first()  # 详情
            # print(name, link, photo, price, detail)

            book = ScrapyDangdangItem(name=name, link=link, photo=photo, price=price)

            # 获取到一个book就将数据交给pipelines,使用管道下载数据
            yield book

        # 每一页的逻辑都是一样的，所以只需要重复调用parse方法
        if self.page <= 100:
            self.page += 1
            url = self.base_url + str(self.page) + "-cp01.01.02.00.00.00.html"
            # 使用以下方法调用parse方法，其中scrapy.Request就是scrapy的get请求
            # url就是执行的地址，callback就是要执行的函数，parse不要加括号
            yield scrapy.Request(url=url, callback=self.parse)
