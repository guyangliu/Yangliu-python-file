import requests
import re

url = 'https://www.pixiv.net/artworks/83250605'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 '
}
page_text = requests.get(url=url, headers=headers, proxies='https://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIkhvbHktVFctSGluZXQ'
                                                           'iLA0KICAiYWRkIjogInR3MDEuaXB2Mi54eXoiLA0KICAicG9ydCI6ICIyMz'
                                                           'MzMyIsDQogICJpZCI6ICJERjdCNzVFQy0wMzU1LTVDMDYtMjI2OC0yRjg4R'
                                                           'DBFQzMwOEQiLA0KICAiYWlkIjogIjAiLA0KICAibmV0IjogInRjcCIsDQog'
                                                           'ICJ0eXBlIjogIm5vbmUiLA0KICAiaG9zdCI6ICIiLA0KICAicGF0aCI6ICI'
                                                           'iLA0KICAidGxzIjogIiINCn0=').text

# # 使用聚焦爬虫对pixiv页面中的图进行解析/提取
# ex = '<div class="rp5asc-9 jDfaKM">.*?<img src="(.*?)"alt.*?</div>'
# img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)
