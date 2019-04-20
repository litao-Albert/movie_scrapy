#链表 数据结构

class Node:
	def __init__(self,value,next):
		self.value,self.next = value,next

a = Node(1,Node(2,Node(3,None)))