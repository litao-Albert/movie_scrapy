# while True:
#     try:
#       x=int(input('请输入一个数字:'))
#     except (TypeError,ValueError) as e:
#         print(e)
#     else:
#         print('没有问题')
#         break
#     finally:
#         print('ssd')
# try:
#     name=input('请输入变量名称：')
#     if name.isdigit():
#         raise NameError('bad name')
# except NameError as e:
#     print(e)
