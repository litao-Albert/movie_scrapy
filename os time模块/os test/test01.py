"""
作业： 写两个py文件test01,test02，test01.py  里面封装两个函数，第一个函数调用时会打印乘法表（for循环），第二个函数调用时会打印三角星。
	要求，test01 自己运行时会打印三角星，而被人导入调用时，只能够调用一个函数方法，只能够打印乘法表。
"""
def test1():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d*%d=%d\t'%(j,i,j*i),end=' ')
        print()
def test2(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end=' ')
            j += 1
        print('')
        i += 1
if __name__ == "__main__":
    test2(5)