# Generated by Django 2.1.4 on 2020-03-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='Active', max_length=255),
        ),
    ]
