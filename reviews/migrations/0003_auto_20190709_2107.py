# Generated by Django 2.2.3 on 2019-07-09 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
