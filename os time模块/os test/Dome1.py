import os
"""
 Python 系统路径和其他一些操作模块
os  常用功能

os.sep()   符合当前系统的路径分隔符，linux/windows\
os.name()  返回操作系统类型Windows "nt" Linux "posix"
os.getcwd()返回当前的工作目录
os.listdir()列出指定目录下的目录文件
os.chdir()  修改当前的工作路径
os.mkdir()  创建目录
os.makedirs() 递归创建目录
os.remove()  删除文件
os.rmdir()   删除文件夹
os.removedirs() 递归删除文件夹
os.system()    执行系统命令
os.popen()     执行系统命令，会将结果以文件的形式返回
os.path.isfile()
os.path.isdir()
os.path.exists()
os.path.split()
"""
# 实现计算文件中的大写字母数
"""
1、把文件给读出来，然后遍历它在计数
"""
# os.chdir('D:\\') # 修改当前的工作路径
with open('D:\\a.txt') as  f :
    l = f.readline()
    print(l)
    count=0
    for i in l:
        if i.isdigit():
            count+=1
    print(count)

print(os.listdir())