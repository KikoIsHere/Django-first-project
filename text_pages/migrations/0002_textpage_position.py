# Generated by Django 3.2.4 on 2021-06-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpage',
            name='position',
            field=models.CharField(choices=[('home', 'Home'), ('footer', 'Footer')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]
