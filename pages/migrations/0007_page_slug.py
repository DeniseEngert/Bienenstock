# Generated by Django 2.1.4 on 2019-01-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190102_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=60),
        ),
    ]