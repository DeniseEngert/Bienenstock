# Generated by Django 2.1.4 on 2019-01-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='about_text',
            field=models.CharField(max_length=4999, verbose_name='about_text'),
        ),
    ]
