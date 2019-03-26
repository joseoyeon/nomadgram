# Generated by Django 2.0.13 on 2019-03-26 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190327_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
