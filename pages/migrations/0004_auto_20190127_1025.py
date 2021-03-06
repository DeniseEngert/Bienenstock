# Generated by Django 2.1.5 on 2019-01-27 10:25

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190127_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='teaser_en',
            field=models.CharField(blank=True, max_length=100, verbose_name='teaser (EN)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_en',
            field=markupfield.fields.MarkupField(rendered_field=True, verbose_name='text (EN)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title_en',
            field=models.CharField(default='', max_length=30, verbose_name='title (EN)'),
        ),
    ]
