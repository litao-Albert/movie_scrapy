import requests
import json
import re
from  requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import  BeautifulSoup
import os
from hashlib import  md5
# 全部图片的页面
def get_page_index(keyword):
    data = {
        'keyword':keyword,

    }
    url ='https://www.toutiao.com/search/?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("请求索引出错")
        return None
#用来解析全部网页的函数
def parse_page_index(html):
    data = json.load(html) # 转换成json的格式
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url') #得到页面的url
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("请求详情页出错",url)
        return None
def parse_page_detail(html,url):
    soup =BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery=(.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.dumps(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images ]
            for image in images:download_image(image)  # 图片下载下来的时候调用下载函数的download
            return {
                'title':title,
                'url':url,
                'image':images
            }
def save_image(content):
    file_path = '{0}/{1}{2}'.format(os.getcwd(),md5(content).hesdigext(),'jpg')
    if os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()
def download_image(url):
    print("正在下载",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return  None
    except RequestException:
        print("请求图片出错")
        return None
def main():
    html = get_page_index('街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            print(result)

if __name__ == '__main__':
    main()
