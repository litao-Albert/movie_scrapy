#coding:utf-8

import datetime
import sys
def writerLog(level,content):
    with open("zabbix.log",'a') as f:
        now = datetime.datetime.now()
        line = "%s[%s]%s;\n"%(now,level,content)
        f.write(line)
        print(content)
        return line
if __name__ == '__main__':
    level = sys.argv[1]
    content = sys.argv[2]
    writerLog(level,content)