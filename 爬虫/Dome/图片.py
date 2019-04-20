import os  #同来创造文件夹
import requests # 发送请求和得到响应用的
from bs4 import BeautifulSoup #用来解析回应的 数据

def GetHtmlText(url):   #得到响应的数据
    try:
        s = requests.session()
        r = s.get(url)
        r.raise_for_status()#判断是否成功
        return r.text  #返回他的响应数据
    except:
        return ' '
def main(pages):  # pages要爬去的图片
    # filepath = os.getcwd() +'\爬的图片\\' #创造一个文件夹用来存照片
    # if not os.path.exists(filepath):  # 加一个判断没有这个文件夹才创造
    #     os.makedirs(filepath)
    pagenum = pages # 要爬去的页数
    fnum = 1
    for page in range(pages):
        url = "https://movie.douban.com/celebrity/1048000/photos/?type=C&start="+str(page*30)+'&sortby=like&size=a&subtype=a'
        url1 = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=xingg'
        html = GetHtmlText(url)
        soup = BeautifulSoup(html,'html.parser') # html.parser是解析器
        #print(soup)
        uls =  soup.find_all('ul',class_="poster-col3 clearfix") # 从响应的数据中找到ul class 是 图片的数据 得到一个列表

        #print(uls)
        for ul in uls:
            imgs = ul.find_all('img') # 找到img的标签  得到一个列表
            #print(imgs)
            print("*"*100)
            for img in imgs:
                imgurl = img['src'] #得到img的 url
                #print(imgurl)
                #print("+"*100)
                imgcontent = requests.get(imgurl).content #得到这个url下的内容connent 应该是二进制的
                print(imgcontent)
                filename = str(fnum) + '.jpg'
                filepath = 'D:\\周杰伦'
                with open(filepath+filename,'wb') as f:
                    f.write(imgcontent)
                    fnum+=1
if __name__ == '__main__':
    main(2)
