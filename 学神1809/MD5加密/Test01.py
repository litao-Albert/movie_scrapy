import hashlib
user = {
    "username":"admin",
    "password":"123456"
}
name = input("请输入用户；")
print(user["username"]== name)
print(user["password"])
# class Test_login(object):
#
#     def __init__(self ,username,password):
#         self.username = username
#         self.password = password
#     def login(self):
#         # md5 = hashlib.md5()
#         # md5.update(self.password.encode('utf-8'))
#         # password = md5.hexdigest()
#         # print(password)
#
#         if self.username == user["username"] and self.password == user["password"]:
#             print("欢迎进入LOL世界！")
#
#         else:
#             print("用户名或者密码错误")
#
#
# if __name__ == '__main__':
#     user = input("请输入用户名：")
#     pwd = input("请输入密码；")
#     T = Test_login(user,pwd)
#     T.login()
