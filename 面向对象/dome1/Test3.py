place = '冥王星'
class Human: #配方，菜单，模型，属性集合
	place = '地球' #共有的变量
		#属于Human的place
	def __init__(self,name,skill):
		print("创建人类")
		self.name = name
		self.skill = skill
		self.attr = '四肢'
		self.attr_1 = '五官'
		self.place = '火星' #覆盖了
		#self 声明我在类中的定义的属性 是属于谁的(实例)
		#self 其实就是每一个创建出来的实例
			#实例标记
	def run(self): #只有人才可以跑
		print('%srun' % self.name)
#Human : 人类属性的抽象集合
	#Human不是一个具体的人
place = '冥王星' #属于全局的place
h1 = Human('亚当','耕田') #0x0000022282737940
	#skill
#类名加括号：实例化
	#h1: 就是一个实例
h2 = Human('夏娃','织布') #0x00000222828B4A90
	#skill
print('移民前:')
print('名字:%s,技能:%s,居住地:%s' % (h1.name,h1.skill,h1.place) )
print('名字:%s,技能:%s,居住地:%s' % (h2.name,h2.skill,h2.place) )
print('移民后:')
#Human.place = '月亮'
	#因为这不是你们独立私有的
h1.place = '月亮'
"""
	这就成了h1私有的
	当使用实例去修改一个属性，那么这个属性直接会升级成私有属性
	你已经把这个大家共享的，认定成了自己私有的，就别想再和大家一样了
	开公司：大家都共享 股份
	私有了，股份变现 退股
	私有了 自己分化公司 成了其他公司
	那之前的公司还和你有关系吗？
"""
Human.place = '火星'

h1.skill = '打猎'
#如果两者都共享place，那么我修改了place
	#是不是以下两者都会修改
print('名字:%s,技能:%s,居住地:%s' % (h1.name,h1.skill,h1.place) )
print('名字:%s,技能:%s,居住地:%s' % (h2.name,h2.skill,h2.place) )
#h1: 实际的人 实例
#Human: 抽象集合 类

#实例中有啥：
	#name
	#skill
	#attr
	#attr_1
	#四个属性是独立的还是共有的?

#水壶都一样：害怕水壶被别人拿错。把你的二维码贴到水壶上
	#信佛 有缘


#argparse
#optparse 命令行传参