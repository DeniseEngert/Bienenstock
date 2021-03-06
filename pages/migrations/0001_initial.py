# Generated by Django 2.1.5 on 2019-01-19 12:20

from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('teaser', models.CharField(blank=True, max_length=100)),
                ('text', markupfield.fields.MarkupField(rendered_field=True)),
                ('text_markup_type', models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='markdown', editable=False, max_length=30)),
                ('slug', models.SlugField(max_length=60)),
                ('_text_rendered', models.TextField(editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
