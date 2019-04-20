# coding:utf-8
import sys
import UI.subUI as f
import UI.DA_ba as d

def MainUi():
    print('---------欢迎使用蜗牛ATM无限制存取系统----------')
    print('---------请选择你的选选项 1：登录 2：注册 3：退出')
    print('-----------------------------------------------')
    choice=int(input("请选择选项："))
    if choice==1:
        doLogin()
    elif choice==2:
        doReygister()
    elif choice==3:
         print('已经退出系统，欢迎使用')
         doQuit()
    else:
         print('你输入错误，拜拜')
def doLogin():
     for i in range(3,0,-1):
       user=input('请输入用户名：')
       user_de=d.select_one_sql('select * from user where user="%s"'%user,databasename='woniuxu')
       if user_de==():
           print('用户名错误！你还有',(i-1),'次')
           continue
       else:
           passwd=input('请输入密码：')
           if user_de[0][1]==passwd:
            print('登录成功')
            f.subUI(user_de)
           else:
              print('密码错误')
     return user_de
def doReygister():
     for i in range(3,0,-1):
        a=input('请输入注册账号:')
        user_de=d.select_one_sql('select * from user where user="%s"'%a,databasename='woniuxu')
        # 如果这个列表中没有数据，为空时，就给里面添加数据就是注册
        if user_de==():
           b=input('请输入注册密码：')
           b1=input('请确认密码：')
           if b==b1:
            c=input('请输入注册金额：')
            e=d.execute_sql('insert into user values("%s","%s","%s")'%(a,b,c),databasename='woniuxu')
            print('恭喜注册成功')
            MainUi()
           else:
               print('你输入的密码不一致')
               continue
        else:
            print('该账户已经存在')


def doQuit():
    sys.exit()
MainUi()
