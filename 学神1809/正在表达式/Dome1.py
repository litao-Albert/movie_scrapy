#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/10/24 10:23
# software:PyCharm Community Edition
import re
# 匹配自身
# a = re.findall(r'abc','abc')

# \为转义字符，将后面得字符改变原有得语义
# a = re.findall(r'a\.c','a.c')
# 匹配任意字符
# a = re.findall(r'a.c','abc')
#字符集，里面得字符可以看成b or c or d
# [A-Z] [a-z] [0-9]
# a = re.findall(r'a[abc]c','abc')
#\d匹配数字字符
# a = re.findall(r'a\dc','a0c')
#\D匹配非数字字符
# a = re.findall(r'a\Dc','ahc')
# \s匹配空字符，或者是\n\t\v（换行，制表符）
# a = re.findall(r'a\sc','a c')
#\S 匹配非空字符相当于【^\s】
# a = re.findall(r'a\Sc','agc')
#\w 匹配单词字符【A-Z,a-z.0-9】
# a = re.findall(r'a\wc','aAc')
# \W匹配非单词字符
# a = re.findall(r'a\Wc','a#c')
# * 匹配前一个字符0或无限次
# a = re.findall(r'abc*','abccc')
# + 匹配前一个字符1次或无限次
# a = re.findall(r'ab+c','abbbbccccc')
# {m} 匹配前一个字符m次
# a = re.findall(r'abc{2}','abccccc')
# {m,n}匹配前一个字符得m次到n次
# a = re.findall(r'abc{1,6}','abcccccccc')
# print(a)
# \A仅匹配字符串开头
# a =re.findall(r'\Aabc','abc')
# ['abc']
# a=re.findall(r'\Aabc','abcdef')
# ['abc']
# # \Z 仅匹配字符串结尾
# a= re.findall(r'def\Z','abcdef')
# ['def']
# #匹配\w和\W之间
# a=re.findall(r'a\b#bc','a#bc')
# ['a#bc']
# #相当于[^\b]
# a=re.findall(r'a\Bbc','abc')
# ['abc']
# # f=re.findall(r'abc|def','adcdef')
# print(f)
# h =re.findall(r'abc|def','abcdef')
# print(h)
# temp = '123 hello world'
#
# ret = re.match(r'\d+',temp)
# if ret:
#     print(ret.group())

temp = '''first line
second line
third line
'''
#将正在表达式编译为pattern对象
# pat = re.compile('.+',re.S)
# print(type(pat))
# print(pat)
# #使用match匹配文本，获取匹配结果，我发匹配时返回None
# result = pat.match(temp)
# #判断是否有结果，如果有结果进行判断操作
# if result:
#     #获取分组信息
#     print(result.group())

temp1 = 'hello world 123'
ret1 = re.search(r'\d+',temp1)
if ret1:
    print(ret1.group())

a = re.findall(r'\d+',temp1)
print(re.split(r'\d',temp1))
print(a)