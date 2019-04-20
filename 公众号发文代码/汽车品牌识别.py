from aip import AipNlp
from aip import AipImageClassify
""" 你的 APPID AK SK """
APP_ID = '10933367'
API_KEY = 'fTUW2Kkk9l0CB8zPFua1f3Ue'
SECRET_KEY = 'CNgFXI8eCds2u5lOFth0OKSIu71dBgNW'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
def compare_words(word1,word2,method):
    if method == 1:
        for word1 in word_list:
            res = client.wordSimEmbedding(word1, word2)
            print([word1, word2, res["score"]])
    elif method==2:
        for word1 in word_list:
            res = client.simnet(word1, word2)
            print([word1,word2,res["score"]])
word_list = ["good","happy","happiness","bad","smile"]
word2 = "beautiful"
method=2
# compare_words(word_list,word2,method)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('222.png')

""" 调用车辆识别 """
print(client.carDetect(image,options = {"top_num":1})["result"][0]["name"])

