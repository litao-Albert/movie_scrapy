"""装饰器的定义：
装饰器是程序开发中经常会用到的一个功能，用好了装饰器，开发效率如虎添翼，当我们已经写好一个函数时，
项目也已经上线，突然客户想要增添一个需求，让这个函数处理更加细致，这个就可以用到装饰器了
"""
def out(info):
    def dec(func):
        def inner(name):
            print('info%s'%name)
            func(name)
            print('come from china')
        return inner
    return dec

@out('装饰器')
def func1(name):
    print('this is %s'%name)
@out('装饰器')
def func2(name):
    print('this is %s'%name)
func1('litao')
func2('json')