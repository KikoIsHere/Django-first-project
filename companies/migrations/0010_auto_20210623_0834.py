# Generated by Django 3.2.4 on 2021-06-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20210618_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='companie',
            name='description_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companie',
            name='description_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companie',
            name='title_bg',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companie',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
