# Generated by Django 2.1.4 on 2020-03-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20200317_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
