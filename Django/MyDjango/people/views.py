from django.shortcuts import render,HttpResponse
from .models import Money
# Create your views here.
def index(request):
    """
    从数据库里提取
    :param request:
    :return:
    """
    date_ = Money.object.all()[0] #所有数据库里的数据都出来吧
    content= {
        'today_info':date_
    }
    return render(request,'test_app/index.html',content)
