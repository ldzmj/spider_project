# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# 如果想使用管道的话，就必须在settings中开启管道
class ScrapyDangdangPipeline:
    # 在爬虫文件开始之前打开文件
    def open_spider(self, spider):
        self.fp = open("book.json", 'w', encoding="utf-8")

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        self.fp.write(str(item))
        # 这种写文件方式不推荐，每传递一个对象就打开一次文件，操作过于频繁
        # 应该在写之前打开文件，写之后关闭，这样就只打开文件一次

        # with open("book.json", 'a', encoding="utf-8")as fp:
        #     fp.write(str(item)) # write方法必须写的是字符串，不能是其他的类型，所以强制转换str
        return item

    # 在文件写完之后再关闭文件
    def close_spider(self, spider):
        self.fp.close()


import urllib.request

# 多管道下载，模仿上面的管道再定义一个管道，在settings添加开启
# 下载图片
class ScrapyDangdangPipeline_photo:
    def process_item(self, item, spider):
        url = "http:" + item.get("photo")
        filename = "./book_photo/" + item.get("name") + ".jpg"
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
