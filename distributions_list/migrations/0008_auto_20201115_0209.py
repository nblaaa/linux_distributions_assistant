# Generated by Django 3.1.3 on 2020-11-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributions_list', '0007_auto_20201115_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributions',
            name='icon',
            field=models.ImageField(upload_to='distributions_list/media/distributions_list/', verbose_name='Изображение'),
        ),
    ]
