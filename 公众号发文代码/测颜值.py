from aip import AipFace
""" 你的 APPID AK SK """
APP_ID = '10960498'
API_KEY = 'ZnxIUPA2Fn83fRVEp4eGkBCz'
SECRET_KEY = 'OwXiwy4CoOPuNxoG5xfdb8zV3SrBK7TT'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)



img1="1.jpg"
img2="2.jpg"
img3="3.jpg"
img4="4.jpg"
img5="5.png"
url_dict={"A某某":img1,"B某某":img2,"C某某":img3,"D某某":img4,"E某某":img5}

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for key,value in url_dict.items():
    # print(key,value)
    image = get_file_content(value)
    """ 调用人脸识别 """
    r = client.detect(image,options = {"face_fields":"age,gender,beauty,qualities"})
    # print(r["result"])
    for i in r["result"]:
        if i["beauty"]>=90:
            print("{} 颜值 {} 优秀".format(key,i["beauty"]))
        elif i["beauty"]>=80:
            print("{} 颜值 {} 良好".format(key,i["beauty"]))
        elif i["beauty"]>=70:
            print("{} 颜值 {} 中等".format(key,i["beauty"]))
        elif i["beauty"]>=60:
            print("{} 颜值 {} 及格".format(key,i["beauty"]))
        elif i["beauty"]<60:
            print("{} 颜值 {} 不及格".format(key, i["beauty"]))



