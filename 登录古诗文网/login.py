import os
import ddddocr
import requests
from lxml import etree

# 古诗文网登录网址
url = "https://so.gushiwen.cn/user/login.aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
# 网页为get请求，跟后面登录时的方法不一样为post，可以先输错密码测试
response = requests.get(url=url, headers=headers)
html = response.text
# with open("login.html", 'w', encoding='utf-8')as fp:
#     fp.write(html)
'''
在响应体login.aspx中有以下数据,其中email和pwd为账号和密码不可能会变，code为验证码，denglu为按钮，只有前两个不知道是什么
但是在网页源码中可以找到对应值得规律，为隐藏域（很重要，反扒手段！！！！）
# __VIEWSTATE: jVPiva0usuyMMvVVcSRusRvE9HasKZG7oR40zHcAb2ZdmTsZCc/H8kmNs2w8M+eS9Cdg0040HX+T0W/2ur4KexotM4RGeGL0Z8dUIgq4c4RlIdkpn8IuXICbiaPnMKI373vtVfAq3swQZIyCNS1OxYlLjy8=
# __VIEWSTATEGENERATOR: C93BE1AE
# from:
# email: 1486300454@qq.com
# pwd: sfgsgg
# code: rzm2
# denglu: 登录
'''
tree = etree.HTML(html)
# 获取__VIEWSTATE的值
__VIEWSTATE = tree.xpath("//body/form/div[1]/input/@value")[0]
# 获取__VIEWSTATEGENERATOR
__VIEWSTATEGENERATOR = tree.xpath("//body/form/div[2]/input/@value")[0]
# 获取验证码图片
code_link = "https://so.gushiwen.cn" + tree.xpath('//img[@id="imgCode"]/@src')[0]  # 图片链接

# 有坑！！！
# 如果用这种方法下载验证码，相当于再次打开这个网页，那么后面再次请求连接的验证码就不同了，就是两个验证码了！！！
# urllib.request.urlretrieve(url=code_link, filename="验证码.jpg")  # 下载验证码
# 所以使用下面的方法：
# requests有一个方法session,通过session的返回值，可以请求变成一个对象
session = requests.session()
code_response = session.get(code_link)  # 验证码的url的内容
code_photo = code_response.content  # 因为图片为二进制，故使用content而不是text

# 下载到本地
with open("验证码.jpg", 'wb')as fp:
    fp.write(code_photo)

# 方法一，手动识别图片输入
# os.startfile("验证码.jpg")  # 自动打开验证码图片
# code = input("请输入验证码：")
# os.remove("验证码.jpg")  # 删除验证码图片

# 方法二，使用ddddocr自动识别验证码
ocr = ddddocr.DdddOcr()
with open("验证码.jpg", "rb")as fp:
    code_img = fp.read()
code = ocr.classification(code_img)
print(code)

# os.remove("验证码.jpg")  # 删除验证码图片

# 登录信息
data = {
    "__VIEWSTATE": __VIEWSTATE,
    "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
    "from": None,
    "email": "1486300454@qq.com",
    "code": code,
    "denglu": "登录"
}
# 登录的时候为post请求，且不能使用requests请求了，否则也是相当于重新打开了网页，就不是原来的网页了
# 需使用session
response_post = session.post(url=url, data=data, headers=headers)
html_post = response_post.text
with open("success.html", 'w', encoding="utf-8")as fp:
    fp.write(html_post)

print("登陆成功！")

# 难点: 1.隐藏域 2.验证码
