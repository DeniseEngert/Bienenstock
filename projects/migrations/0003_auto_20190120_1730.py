# Generated by Django 2.1.4 on 2019-01-20 16:30

from django.db import migrations, models
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190120_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data_file',
            field=models.FileField(null=True, upload_to='csv/', validators=[projects.validators.validate_csv], verbose_name='data_file'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='title'),
        ),
    ]
