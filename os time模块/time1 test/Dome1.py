import time
import  datetime
"""
time 模块
时区    UTC0时区（中国东八区：上海）
海秒    是61秒（地球自转偏差导致的多出的1秒）
时间戳  1970年1月1日 0：00（距离上面这个时间过了多少秒）
夏令时  夏令时日光时为了节省能源，每年夏天人工将时间调早一个小时
0，1，-1 采用，不采用，有系统判断

时间的格式
1、字符串时间
2、九元素时间
1、年tm_year  
2、月tm_mon 
3、日tm_mday 
4、时tm_hour 
5、分tm_min 
6、秒tm_sec1-61 
7、一周的第几天tm_wday0-6
8、一年的第几天tm_yday
9、是否夏令时tm_isdst1启用0 不启用-1

3、时间戳
time.localtime()  返回当前时区的九元素时间
time.gmtime()     返回0时区的九元素时间
time.struct_time()将一个九元素元组转换成时间
time.asctime()    将九元素时间转换成字符串格式周月日时分秒年
time.ctime()      将时间戳转换成字符串时间周月日时分秒年
time.strftime()   定制指定格式字符串时间
time.time()       返回当前时间的时间戳
time.mktime()     返回九元素时间的时间戳
time.clock()      在Linux下记录进程运行时间，在win下记录是距离上一次调用过了多久
time.sleep()      就是让程序挂起指定秒
"""
# time1 = time.ctime()
# time2 = time.localtime()
# time3 = time.gmtime()
# time4 = time.strftime("%H:%M:%S")
# # time5 = time.struct_time()
# time6 = time.asctime()
# print(time1)
# print(time2)
# print(time3)
# print(time4)
# # print(time5)
# print(time6)
"""Python：输入年月日判断是此年的第多少天"""
# 今天日期减去去年12月31日的日期即可
y = int(input('请输入4位数数字的年份：'))  #得到年份
m = int(input('请输入月份：'))             # 得到月份
d = int(input('请输入是那一天：'))          # 得到是那一天
tagetDay = datetime.date(y,m,d) # 将输入的日期格式化成标准的日期
l = tagetDay.year # 得到输入的年
lastDay = datetime.date(l - 1,12,31)    # 得到上一年的最后一天

dayCount = tagetDay - lastDay # 减去上一年的最后一天就是这一天是此年的第多少天
print('%s是%s年的第%s天'%(tagetDay,y,dayCount.days))
"""
4、strftime的格式符
%y 两位
%Y 四位
%m 月
%d 日
%H24时
%l12时
"""