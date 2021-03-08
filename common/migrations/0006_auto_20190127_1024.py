# Generated by Django 2.1.5 on 2019-01-27 10:24

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20190127_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='about_text_en',
            field=markupfield.fields.MarkupField(blank=True, rendered_field=True, verbose_name='about_text (EN)'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='contact_en',
            field=models.CharField(blank=True, max_length=300, verbose_name='contact (EN)'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='description_en',
            field=models.CharField(blank=True, max_length=300, verbose_name='description (EN)'),
        ),
    ]