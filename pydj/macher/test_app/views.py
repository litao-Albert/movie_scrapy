from django.shortcuts import render,HttpResponse
from .models import Money
# Create your views here.

def index(request):
    """
    从数据库里面去
    :param request:
    :return:
    """
    date_ = Money.object.get()[0]
    conyent = {'today_info':date_}
    return render(request,'test_app/index.html',conyent)
