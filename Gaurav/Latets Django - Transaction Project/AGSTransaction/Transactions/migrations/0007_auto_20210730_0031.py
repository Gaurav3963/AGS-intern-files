# Generated by Django 3.2.5 on 2021-07-29 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0006_auto_20210730_0025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='TranDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 30, 0, 31, 1, 924745)),
        ),
        migrations.AlterField(
            model_name='transactiondetails',
            name='transData',
            field=models.TextField(),
        ),
    ]
