# Generated by Django 2.2.6 on 2020-10-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201018_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=255),
        ),
    ]