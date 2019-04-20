import requests
class start:
        def __init__(self):
            self.url = 'http://localhost/upload/register.php'
            self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        def add_user(self):
            for number in range(1,300):
                a =str(number)
                b = 'texst'
                c = b+a
                d = "123458"
                mail =d+a +'@qq.com'
                data1={'forward=':'','step':'2','regname':c,'regpwd':'123456','regpwdrepeat':'123456','regemail':mail,'rgpermit':'1'}
                s = requests.session()
                a = s.post(self.url,data=data1)
                a.encoding='utf-8'
                if '注册成功'in a.text:
                    print('注册成功')
                else:
                    print('注册失败')
start().add_user()

