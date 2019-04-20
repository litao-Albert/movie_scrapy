import wx
"""
# 创建主循环
app = wx.App()
# 创建窗口组件
frame = wx.Frame(None)
    # parent=None, 父元素，指当前组件的父元素,如果父元素为None代表组件为顶级组件
    # id=None  组件的标识，同一个图形化当中，同样的id只允许出现一次，但是默认id为-1，系统分配的
    # title=None 组件的标题
    # pos=None    组件的位置，pos是一个二维的坐标，是组件左上角的二维坐标
    # size=None  组件的大小
    #style=None  组件的样式 ，官网有完整的样式表
    # name=None  组件的标识，通常用于传参
text = wx.TextCtrl()
    # parent=None, 父元素，指当前组件的父元素,如果父元素为None代表组件为顶级组件
    # id=None  组件的标识，同一个图形化当中，同样的id只允许出现一次，但是默认id为-1，系统分配的
    # value = None, 文本框的值
           # Getvalue 获取值
           # Setvalue 设置值
    # pos=None.组件的位置，pos是一个二维的坐标，是组件左上角的二维坐标
    # size=None 组件的大小
    #style=None 组件的样式，官网有完整的样式表
    # validator=None 校验数据
    # name=None 组件的标识，通常用于传参
button = wx.Button()
    # parent=None, 父元素，指当前组件的父元素,如果父元素为None代表组件为顶级组件
    # id=None  组件的标识，同一个图形化当中，同样的id只允许出现一次，但是默认id为-1，系统分配的
    # label = None, 按钮的标签，就是按钮上的文字
    # pos=None.组件的位置，pos是一个二维的坐标，是组件左上角的二维坐标
    # size=None 组件的大小
    # style=None 组件的样式，官网有完整的样式表
    # validator=None 校验数据
    # name=None 组件的标识，通常用于传参
# 调用窗口的显示
frame.Show()
# text.Show()
# button.Show()
#启动主循环
app.MainLoop()

"""
#  定义功能函数（打开和关闭）
def opens(event):    #打开函数
    path = path_text.GetValue()
    with open(path,"rb") as f:
        content = f.read()
        content_text.SetValue(content)
def saves(event):    #保存函数
    path = path_text.GetValue()
    with open(path,"wb") as f:
        content = content_text.GetValue()
        f.write(content.encode())

app = wx.App()  # 创建主循环
frame = wx.Frame(None,title = 'litaos editor',pos = (200,200),size = (800,500))  # 创建窗口组件
path_text = wx.TextCtrl(frame,pos = (5,5),size = (324,24))
open_button = wx.Button(frame,label = "打开",pos = (410,5),size = (70,24))
# 绑定函数事件
open_button.Bind(wx.EVT_BUTTON,opens)
save_button = wx.Button(frame,label = "保存",pos = (330,5),size = (70,24))
# 绑定函数事件
save_button.Bind(wx.EVT_BUTTON,saves)
content_text = wx.TextCtrl(frame,pos = (5,39),size = (470,410), style = wx.TE_MULTILINE)
frame.Show() # 调用窗口的显示
app.MainLoop()  #启动主循环