# Generated by Django 2.2.6 on 2020-10-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201018_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
