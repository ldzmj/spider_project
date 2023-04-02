import urllib.request
from lxml import etree


# 1.源码获取
def url_get(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Cookie": "cz_statistics_visitor=c17b62a9-5008-ca0f-e41b-6b9a7eaec598; __bid_n=186eeb0db021135ec54207; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1679041813; FPTOKEN=umc5vVdnXdcZnlhBopXakUfGvShHAs6jIyYXnQtBB8neD841jjlS/DUYW2hm4Gc7DX0gV4oHhJxh6GugPy2gFjJJP/ChWfOWrPTnCcnZ+Kv1BpRZoPfQ7i1/eLSfTke+AGT7QR5R8rEY+VEIjtCppSZPvcWSpyQCI9b3pEQpz+3RX7Sbk2ngJj5/ZCNd5Z6iRIBQFRCD3fR4DwHehwmrMkpb1q8NNvFzkclpOx8DB/+cUVCgVpJBz1hCHFDHI/LhHdbbwyx4ECcE4VomH7LA/lubZAsdAZKnzqmB9F1TIXRugDOFrGIPe/3+sCyENhzLzFEg3hrm+F2ycXizpowoxijW/ume6vEmhykIQNOLXEz12wUtV93RMHDQ1pe6B9xQOiXCFJGGk9/GneZIDhm2KUMhT/T1VWXYjyWHGA76Wh6YAEfIAK8R4CC+LtdLPym6|8KZe6fiUUYRUa9EaKnG9Sws8ydL5cQ/T28ty6i2HgoM=|10|a4bd14e655a377e391ab600bf5ef2ccc; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1679042660"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html


# 2.图片信息获取
def data_get(html):
    tree = etree.HTML(html)
    data = {}  # 存放名字和图片
    photo = []  # 存放图片
    photo_link = tree.xpath("//img/@data-original")  # 图片
    name = tree.xpath("//img/@alt")  # 图片名
    # photo返回的没有https:前缀，给每个链接加前缀
    for item in photo_link:
        item = "https:" + item
        photo.append(item)
    # 将图片和名字存入info中
    for i in range(0, len(photo)):
        data[name[i]] = photo[i]
    # print(info)

    return data


# 3.下载图片
def download(data):
    for k, v in data.items():
        urllib.request.urlretrieve(url=v, filename="图片/" + k + ".jpg")  # 下载


if __name__ == '__main__':

    '''
    # 第一页 https://sc.chinaz.com/tupian/fengjing.html
    第二页 https://sc.chinaz.com/tupian/fengjing_2.html
    第三页 https://sc.chinaz.com/tupian/fengjing_3.html
    '''

    base_url = 'https://sc.chinaz.com/tupian/fengjing'
    # 爬取页数
    start = int(input("请输入爬取起始页："))
    end = int(input("请输入爬取终止页："))
    for i in range(start, end+1):
        if i == 1:
            url = base_url + '.html'
        else:
            url = base_url + '_' + str(i) + '.html'
        # print(url)
        # 获取源码
        html = url_get(url)
        # 获取图片信息
        data = data_get(html)
        # 下载
        download(data)
