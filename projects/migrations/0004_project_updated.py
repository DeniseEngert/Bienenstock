# Generated by Django 2.1.4 on 2019-01-07 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_dataset_data_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]