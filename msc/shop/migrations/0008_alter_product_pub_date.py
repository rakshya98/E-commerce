# Generated by Django 4.1.5 on 2023-02-05 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]