# Generated by Django 2.0.13 on 2019-05-01 08:39

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('images', '0002_auto_20190331_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
