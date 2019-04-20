from django.contrib import admin
from .models import Money

# Register your models here.
# 注册数据库中表，到admin界面

admin.site.register(Money)
