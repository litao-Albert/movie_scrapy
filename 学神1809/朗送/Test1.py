# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello,I am the king of the world Hao are you")
import pyttsx3
with open("D:\\a.txt",encoding='utf-8') as f:
  lines = f.readlines()
  print(lines)
  engine = pyttsx3.init()
 #engine.say(lines)
  engine.say('如果你足够快乐，队友的问号就跟不上你，快乐风男，加油吧')
  engine.runAndWait()  # 运行并且等待

# 1、更改声音

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('I am very very love you')
#    engine.runAndWait()
# 2、控制语速
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-100)
# engine.say('啊，哎呦，哎呦我去，哎呦我去')
# engine.runAndWait()
# #  3、控制音量
# import pyttsx3
# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.1)
# engine.say('这是一条神奇的天路哎呦，哎呦不错呦')
# engine.runAndWait()
"""
	实战：上面咱们所说了，可以的对文本进行朗读，那我们结合，爬虫，爬取小说网站，并把网站中的小说内容，写一个程序读取出来呢？
	项目开始之前我们首先要分析：
	第一步：爬取小说网站
	第二步：利用xpth 获取内容
	第三步：利用文件操作生成一个txt文件
	第四步：处理文件内容
	第五步：读取出来
"""