# Generated by Django 3.2.4 on 2021-06-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20210617_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='from_weekday',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='to_weekday',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=50, unique=True),
        ),
    ]
