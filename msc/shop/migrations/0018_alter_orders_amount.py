# Generated by Django 4.1.5 on 2023-02-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]