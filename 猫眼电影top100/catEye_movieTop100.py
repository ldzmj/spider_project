import re
import xlwt
import urllib.request
from bs4 import BeautifulSoup

# 电影名的正则表达式
movie_name = re.compile(r'title="(.*?)"')
# 电影封面链接的正则表达式
movie_photo = re.compile(r'img.*data-src="(.*?)"/>')
# 电影主演
movie_star = re.compile(r'<p class="star">(.*?)</p>', re.S)
# 电影上映时间
movie_releaseTime = re.compile(r'<p class="releasetime">(.*)</p> </div>')
# 电影评分
movie_score = re.compile(r'<p class="score"><i class="integer">(.*)</i><i class="fraction">(.*)</i></p>')
# 存放所有电影信息
movie_info = []


# 1.网页获取
def web_data():
    # 根据网址发现中间有很多网址都是可以删除的，因此可删减为以下网址
    web_url = "https://www.maoyan.com/board/4?timeStamp=1677653488928&offset="
    # 获取每一页网址
    for i in range(0, 10):
        url = web_url + str(i * 10)
        html = data_get(url)
        web_info(html)
        print(f"正在爬取第{i + 1}页")


# 2.网页源码获取
def data_get(url):
    web_url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Cookie": "__mta=141827725.1677653340957.1677655011274.1677655530961.18; uuid_n_v=v1; uuid=256D1C70B7FD11ED965E691062937F3C6DFF3DC57731465D88797A96B9BC6BC4; _csrf=c7c9767067b735120f38acbfb5cf3b36d07375d28664e809440ba16a9d4cb16a; _lxsdk_cuid=1869bee7290c8-08b1f681b1cd4a-26031951-144000-1869bee7290c8; _lxsdk=256D1C70B7FD11ED965E691062937F3C6DFF3DC57731465D88797A96B9BC6BC4; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1677653341; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=141827725.1677653340957.1677653461865.1677653484931.7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1677655531; _lxsdk_s=1869bee7291-3c4-0a9-bfd%7C%7C41"
    }
    request = urllib.request.Request(url=web_url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    # print(html)
    return html


# 对网页进行解析获得数据
def web_info(html):
    # 创建网页解释器
    bs = BeautifulSoup(html, "html.parser")

    for movie in bs.find_all("dd"):
        # print(movie)
        # print("--------------------------------------------------------------------------")
        movie_data = []  # 存放每个电影信息
        movie = str(movie)
        # 电影名
        name = re.findall(movie_name, movie)[0]
        movie_data.append(name)
        # 封面链接
        photo = re.findall(movie_photo, movie)[0]
        movie_data.append(photo)
        # 主演
        star = re.findall(movie_star, movie)[0]
        star = re.sub("(\s+)?", "", star)  # 删除换行符，空格
        star = re.sub("主演：", "", star)
        movie_data.append(star)
        # 评分
        score = re.findall(movie_score, movie)[0]
        score = score[0] + score[1]
        movie_data.append(score)
        # 上映时间
        releaseTime = re.findall(movie_releaseTime, movie)[0]
        movie_data.append(releaseTime)
        # 保存到总表
        movie_info.append(movie_data)


def data_save():
    # 创建一个Excel文档对象
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个工作表
    worksheet = workbook.add_sheet("电影榜单")
    # 设置列名
    col_name = ["电影名", "封面链接", "主演", "评分", "上映时间"]
    for i in range(0, 5):
        worksheet.write(0, i, col_name[i])
    # 写入电影数据
    for i in range(1, 101):
        for j in range(0, 5):
            worksheet.write(i, j, movie_info[i - 1][j])
    # 保存文件
    workbook.save("猫眼电影top100.xls")


if __name__ == '__main__':
    print("开始爬取数据...")
    web_data()
    # print(movie_info)
    print("爬取完毕！")
    print("数据正在保存...")
    data_save()
    print("数据保存完毕！")
