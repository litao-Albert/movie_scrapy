# f=open(r'C:\Xampp\apache\logs\\access.log','r')
# connet=f.read()
# print(connet)
# f.close()
# f1=open(r'C:\Xampp\apache\logs\\error.log','r')
# connet1=f1.readlines()
# print(connet1)
# f1.close()
# f3=open(r'C:\Xampp\apache\logs\\new.log','a')
# sd=f3.writelines(connet1)
# f3.read()
while True:
    try:
        f=open('D:\\text.txt','w')
        s=f.write('asdssdsasd')
        f.close()
    except Exception as e:
        print(e)
        break
