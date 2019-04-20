# import logging
# logging.basicConfig(level = logging.ERROR,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
# logger.error("error")
#
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
import threading,time
import requests,json
from lxml import etree


headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
}
class YM(object):
    def __init__(self,words):
        self.words=words

    def get_words_list(self,words):
        list=[]
        for i in words:
            for j in words:
                for m in words:
                    for n in words:
                        name="{}{}{}{}".format(i,j,m,n)
                        list.append(name)
        return list
    def get_res(self,list):
        try:
            num=-1
            self.res1 = []
            for name in list:
                num=num+1
                try:
                    url = "https://sg.godaddy.com/zh/domainsapi/" \
                          "v1/search/exact?q={}&key=dlp_offer_com&pc" \
                          "=50120152&ptl=1".format(name)
                    con=requests.get(url,headers=headers).text
                    dict=json.loads(con)
                    # print(num,name)
                    if dict["ExactMatchDomain"]["IsAvailable"]==True:
                        self.res1.append(name)
                        print(name)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    def res(self):
        return self.res1


words=list("abcdefghijklmnopqrstuvwxyz")
ym = YM("words")
words_list=ym.get_words_list(words)
print(words_list,len(words_list))
list1=words_list[0:3000]
list2=words_list[3000:6000]
list3=words_list[6000:9000]
list4=words_list[9000:12000]
list5=words_list[12000:15000]
list6=words_list[15000:17576]
t1 = threading.Thread(target=ym.get_res, args=(list1,))
t1.start()
t2 = threading.Thread(target=ym.get_res, args=(list2,))
t2.start()
t3 = threading.Thread(target=ym.get_res, args=(list3,))
t3.start()
t4 = threading.Thread(target=ym.get_res, args=(list4,))
t4.start()
t5 = threading.Thread(target=ym.get_res, args=(list5,))
t5.start()
t6 = threading.Thread(target=ym.get_res, args=(list5,))
t6.start()

