# Generated by Django 3.2.4 on 2021-06-25 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_pages', '0013_auto_20210625_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='name_bg',
        ),
        migrations.RemoveField(
            model_name='navbar',
            name='name_en',
        ),
    ]
