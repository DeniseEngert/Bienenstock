# Generated by Django 2.1.4 on 2019-01-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]