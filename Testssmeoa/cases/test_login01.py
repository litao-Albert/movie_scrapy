from  Testssmeoa.common.login import login
from  Testssmeoa.common.login import Setup
from  Testssmeoa.common.oa_notice import notice
from time import  sleep
class cass:
    ws=Setup().ws #实例化setup对象
    l=login() #调用登录方法
    l.get_wd(ws)  #把driver传给登录的类，执行登录
    # l.input_username('admin') #输入用户名
    # l.input_password('admin') #输入密码
    # l.click_login_button() #点击登录
    driver=l.login_action('admin','admin')
    try:
        ele=driver.find_element_by_link_text('公告').text
        if '公告'==ele:
            print('登录成功')
    except:
        print('登录失败')
cass()

