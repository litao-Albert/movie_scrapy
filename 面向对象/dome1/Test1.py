class myInt(int):
	def __add__(self,num):
		return 1+num+self
	#运算符重载加继承

a = myInt(1)
#print(a)

print('结果:',a + a )