# Generated by Django 3.2.4 on 2021-06-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20210616_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'ordering': ['placement']},
        ),
        migrations.AddField(
            model_name='companies',
            name='meta_description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='companies',
            name='meta_keywords',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='companies',
            name='placement',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
