# Generated by Django 3.0.1 on 2019-12-21 03:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20191220_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpost',
            name='additionalComments',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='cons',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
