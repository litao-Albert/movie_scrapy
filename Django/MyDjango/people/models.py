from django.db import models

# Create your models here.

class Money(models.Model):
    """
    一个类的编写就是一个表
    """
    NewClients = models.CharField(max_length=10)
    TotalSales = models.CharField(max_length=10)
    TodayProfit = models.CharField(max_length=10)
    NewInvoice = models.CharField(max_length=10)
