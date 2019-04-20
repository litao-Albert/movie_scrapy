import UI.DA_ba as d
# import UI.mainUI as dsd
def subUI(user_de):
    print('-------欢迎来到蜗牛学院ATM!-------------------------')
    print('---请输入你的选项 1:查询 2:存钱 3：取钱4：转钱 5:返回主界面')
    print('----------------------------------------------------')
    choice=int(input('请输入你的选项：'))
    if choice==1:
        checkMoney(user_de)
    elif choice==2:
        saveMoney(user_de)
    elif choice==3:
        getMoney(user_de)
    elif choice==4:
        transferMoney(user_de)
    elif choice==5:
         # dsd.MainUi()
          pass
    else:
        print('你输入错误')
        subUI(user_de)
def checkMoney(user_de):
    # 获取当前用户的余额
    money=user_de[0][2]
    print('你的账户余额：',money)
    subUI(user_de)
    # print('-----------1:返回 2：退出————————')
    # sd=input('请输入选项：')
    # if   sd==1:
    #     subUI(user_de)
    # elif sd==2:
    #      quit()
def saveMoney(user_de):
    money=int(input('请输入你需要存的金额：'))
    Summoney=int(user_de[0][2])+money
    d.execute_sql('update user set money="%s" where user="%s"'%(Summoney,user_de[0][0]),databasename='woniuxu')
    print('你已经存入：',money)
    subUI(user_de)

def getMoney(user_de):
     money=int(input('请输入你需要取的金额：'))
     Summoney=int(user_de[0][2])- money
     d.execute_sql('update user set money="%s" where user="%s"'%(Summoney,user_de[0][0]),databasename='woniuxu')
     print('你取了：',money)
     subUI(user_de)

def transferMoney(user_de):
    for i in range(3,0,-1):
        a=input('请输入你转账的账户：')
        user=d.select_one_sql('select * from user where user="%s"'%a,databasename='woniuxu')
        if user==():
            print('该用户不存在,请输入正确的用户')
            continue
        else:
            money=int(input('请输入你的转账金额：'))
            # 获取对方的账户
            # 把转入的钱存入对方的账户
            Summoney1=int(user[0][2])+ money
            d.execute_sql('update user set money="%s" where user="%s"'%(Summoney1,user[0][0]),databasename='woniuxu')
            Summoney=int(user_de[0][2])- money
            d.execute_sql('update user set money="%s" where user="%s"'%(Summoney,user_de[0][0]),databasename='woniuxu')
            print('你给对方转了：',money)
            subUI(user_de)