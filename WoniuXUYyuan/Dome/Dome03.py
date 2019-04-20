import requests
import json
# class count:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mut(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
class count1:
    def test(self,a):
        url='http://127.0.0.1:8000/api/get_event_list/'
        r=requests.get(url,params={'eid':a})
        result=r.json()
        return result

