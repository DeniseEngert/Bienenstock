# Generated by Django 2.1.5 on 2019-01-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190120_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/None/placeUser.png', upload_to='images/', verbose_name='image'),
        ),
    ]
