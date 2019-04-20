# 闭包的定义：
# #
# # 1、闭包函数必须有内嵌函数；
# # 2、内嵌函数需要引用该嵌套函数上一级namespace中的变量
# # 3、闭包函数必须返回内嵌函数；
# # 通过这三点，就可以创建一个闭包；python装饰器就是使用了闭包，闭包的好处，使代码变得简介
#coding:utf-8

def test(number):
    def test_in(number_in):
        print('in test_in函数，number_in is %d'%number_in)
        return number + number_in
    return test_in
ret = test(20)    # 执行test(20),相当于调用test函数，而test函数返回的是test_in,所以test（20）
#=test_in=ret
# 接着调用ret(100)，那ret就是test_in,那ret(100)==test_In(100)
print(ret(100))

