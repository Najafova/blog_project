# Generated by Django 2.1.4 on 2020-03-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20200317_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='Deactive', max_length=255),
        ),
    ]
