from AGSTransaction.settings import MEDIA_ROOT
from django.db import models

# Create your models here.

class TransactionDetails(models.Model):
    tranDate = models.DateField()
    tranTime = models.TimeField()
    tranCardNo = models.CharField(max_length=20)
    tranFromAccount = models.CharField(max_length=20)
    tranTerminalID = models.CharField(max_length=20)
    tranTransactionID = models.CharField(max_length=20)
    tranMerchantID=models.CharField(max_length=20)
    transData = models.CharField(max_length=100)

class FileUpload(models.Model):
    file = models.FileField()


