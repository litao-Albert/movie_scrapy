# def dec(number):
#     def test_in(number_test):
#         print("test in %d"%number_test)
#         return number+number_test
#     return test_in
# a=dec(5)
# print(a(10))
x = 2
def outer():
    x = 0
    def inner():
        nonlocal x
        x = x+1
        print(x)
    print(x)
    return inner
a = outer()
a()