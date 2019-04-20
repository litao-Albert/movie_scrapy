import  re
html = "adasdadadd1131133"
try:
    pattern = re.compile('a.*?(\d+).*?')
    item = re.findall(pattern,html)
    print(item)
except Exception as e:
    print(e)
