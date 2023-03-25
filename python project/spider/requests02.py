import requests

# UA伪装：将对应的User-Agent封装到一个字典中
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 '
}
url = 'https://www.sogou.com/web'
# 处理url携带的参数：封装成为一个字典
kw = input('enter a word:')
param = {
    'query': kw
}
response = requests.get(url=url, params=param, headers=header)
page_text = response.text
FileName = kw + '.html'
with open(FileName, 'w', encoding='utf-8') as f:
    f.write(page_text)
print(FileName + '保存成功！！')
