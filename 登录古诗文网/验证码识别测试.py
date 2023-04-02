import ddddocr


def recognize():
    ocr = ddddocr.DdddOcr()
    with open('验证码.jpg', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)


recognize()
