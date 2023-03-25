import requests

url = 'https://pic.qiushibaike.com/system/pictures/12423/124238410/medium/YG8Z33RG54KR7OC2.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 '
}
# content返回的是二进制形式的图片数据
# .text(字符串)  .content(二进制)  .json()(对象)
img_data = requests.get(url=url, headers=headers).content

with open('qiutu.jpg', 'wb') as fp:
    fp.write(img_data)
