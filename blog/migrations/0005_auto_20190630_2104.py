# Generated by Django 2.0.13 on 2019-06-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190630_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/'),
        ),
    ]
