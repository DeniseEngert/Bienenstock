# Generated by Django 2.1.5 on 2019-01-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190120_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='picture_platzhalter',
        ),
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(default='images/None/placeProject.png', upload_to='images/'),
        ),
    ]
