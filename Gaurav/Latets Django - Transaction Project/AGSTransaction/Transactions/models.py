from AGSTransaction.settings import MEDIA_ROOT
from django.db import models
from datetime import datetime
# Create your models here.

class TransactionDetails(models.Model):
    tranDate = models.DateTimeField(default=datetime.now(),blank=True)
    tranTerminalID = models.CharField(max_length=20)
    tranTransactionID = models.CharField(max_length=20)
    tranMerchantID=models.CharField(max_length=20)
    transData = models.TextField()

class Position(models.Model):
    Column = models.CharField(max_length=100,blank=False)
    Position = models.IntegerField()

class FileUpload(models.Model):
    file = models.FileField()


