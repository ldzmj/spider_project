import sqlite3
import urllib.request
import re
import xlwt
from bs4 import BeautifulSoup

# 电影链接的正则表达式
movie_link = re.compile(r'<a class="" href="(.*?)">')
# 电影名的正则表达式
movie_name = re.compile(r'<span class="title">(.*?)</span>')
# 电影封面的正则表达式
movie_photo = re.compile(r'<img.*src="(.*?)" width="100"/>', re.S)
# 电影一句话概括的正则表达式
movie_summarize = re.compile(r'<span class="inq">(.*?)</span>')
# 电影评分
movie_score = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 电影评价人数
movie_judgeNumber = re.compile(r'<span>(\d*)人评价</span>')

data_info = []  # 全部电影信息


# 2.网页爬取
def url_get(wb_url):
    url = wb_url
    '''
    get请求一个网页
    但是此种方法对于有些网站不能用，对方会禁止爬虫
    # response = urllib.request.urlopen(url)
    # print(response.read().decode("uf-8"))
    '''
    # 用户代理。伪装成电脑，使服务器相信这不是网络爬虫
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Cookie": "douban-fav-remind=1; bid=UuuNwd3FfgE; __utmz=30149280.1677240651.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1677240651.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=JlXvwnKXSdCXMIDf2ZAqPnI87JJpZsTA; __gads=ID=05f848a71be3b908-22cbcf0023da00fc:T=1677240652:RT=1677240652:S=ALNI_MZrE_rradMAOPq7W_CVU2RSxoZGYQ; __utmc=30149280; __utmc=223695111; __gpi=UID=00000bcb773974be:T=1677240652:RT=1677500035:S=ALNI_MZOMFyPSAHOkT9yq1X5NBQQZAtqow; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1677503497%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6pkZ3UZIpVHOeLJkCSu-j8b_0q7mFjErkD23x0GXfOHQowBs2rZwV5hSI9vKj-64%26wd%3D%26eqid%3Dabed860d00057b240000000463f8a93c%22%5D; __utma=30149280.1611782961.1677240651.1677499722.1677503497.4; __utma=223695111.413038286.1677240651.1677499722.1677503497.4; _pk_id.100001.4cf6=8c9121af373af442.1677240651.4.1677505257.1677500141."}
    # 构建一个请求对象request
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    # 获取源码内容
    html = response.read().decode('utf-8')
    # print(html)
    return html


# 1.网页数据获取
def data_get():
    base_url = "https://movie.douban.com/top250?start="
    # 获取每一页的信息
    for i in range(0, 10):
        url = base_url + str(i * 25)
        # 保存获取到每一页的源码
        html = url_get(url)
        # 对每一页进行解析
        pageData_get(html)
    # print(data_info)


# 3.对当前页的数据进行解析
def pageData_get(html):
    # 创建一个解释器，解析网页
    bs = BeautifulSoup(html, "html.parser")
    # 定位到电影信息部分
    # movie = bs.find_all('div', class_="hd")
    for movie in bs.find_all('div', class_="item"):
        # print(movie)
        movie_data = []  # 保存电影信息
        movie = str(movie)

        # 提取电影链接
        link = re.findall(movie_link, movie)[0]
        movie_data.append(link)

        # 提取电影名
        name = re.findall(movie_name, movie)
        if len(name) == 2:
            name_China = name[0]  # 中文名
            name_foreign = name[1]  # 外国名
            name_foreign = re.sub("(\s+)?", "", name_foreign)  # 删除空格
            name_foreign = re.sub("/", "", name_foreign)#删除/
            movie_data.append(name_China)
            movie_data.append(name_foreign)
        else:
            name_China = name[0]
            name_foreign = " "
            movie_data.append(name_China)
            movie_data.append(name_foreign)

        # 提取电影封面
        photo = re.findall(movie_photo, movie)[0]
        movie_data.append(photo)

        # 一句话概括
        summarize = re.findall(movie_summarize, movie)  # 有可能概述为空，所以不能写成[0]
        # 判断是否有概括
        if len(summarize) != 0:
            summarize = summarize[0]
            movie_data.append(summarize)
        else:
            movie_data.append(" ")

        # 评价人数
        judgeNumber = re.findall(movie_judgeNumber, movie)[0]
        movie_data.append(judgeNumber)

        # 评分
        score = re.findall(movie_score, movie)[0]
        movie_data.append(score)
        # print(movie_data)
        data_info.append(movie_data)
    return data_info


# 4.数据保存
def data_save():
    # 创建一个Excel文档对象
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建工作表
    worksheet = workbook.add_sheet("电影榜单")
    col_name = ("中文名", "外国名", "封面链接", "详情链接", "评分", "评价人数", "概括")
    # 设置列名
    for i in range(0, 7):
        worksheet.write(0, i, col_name[i])
    # 写入电影信息
    for i in range(1, 250):
        worksheet.write(i, 0, data_info[i - 1][1])  # 中文名
        worksheet.write(i, 1, data_info[i - 1][2])  # 外国名
        worksheet.write(i, 2, data_info[i - 1][3])  # 封面链接
        worksheet.write(i, 3, data_info[i - 1][0])  # 详情链接
        worksheet.write(i, 4, data_info[i - 1][6])  # 评分
        worksheet.write(i, 5, data_info[i - 1][5])  # 评价人数
        worksheet.write(i, 6, data_info[i - 1][4])  # 概括
    # 保存文件
    workbook.save("豆瓣电影top250.xls")


def data_dbSave():
    db = sqlite3.connect("豆瓣电影.db")
    cursor = db.cursor()  # 游标
    # 建表
    sql_buildTable = '''
        create table movie_top250
        (
        id integer primary key autoincrement,
        China_name varchar,
        foreign_name varchar,
        photo_link text,
        details_link text,
        score numeric,
        appraise_num numeric,
        summarize text
        )
    '''
    cursor.execute(sql_buildTable)
    # 插入数据
    for data in data_info:
        for index in range(0,len(data)):
            if index == 5 or index == 6:
                continue
            else:
                data[index] = '"' + data[index] + '"'
        sql_insertData = '''
            insert into movie_top250(details_link,China_name,foreign_name,photo_link,summarize,appraise_num,score)
            values(%s)''' % ",".join(data)
        # print(sql_insertData)
        cursor.execute(sql_insertData)
        db.commit()

    db.close()


if __name__ == '__main__':
    data_get()
    print(data_info)
    # 保存数据
    # data_save()  # 保存到Excel
    data_dbSave()  # 保存到sqlite数据库中
    print("爬取完毕！")
