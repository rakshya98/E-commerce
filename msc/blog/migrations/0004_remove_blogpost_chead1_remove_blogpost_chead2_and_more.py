# Generated by Django 4.1.5 on 2023-06-27 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head2',
        ),
    ]
