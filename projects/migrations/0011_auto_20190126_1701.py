# Generated by Django 2.1.5 on 2019-01-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190126_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataset',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('updated',)},
        ),
    ]