# Generated by Django 3.2.4 on 2021-06-25 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_pages', '0008_navbar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navbar',
            old_name='display_order',
            new_name='position',
        ),
    ]