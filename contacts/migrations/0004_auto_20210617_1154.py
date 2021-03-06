# Generated by Django 3.2.4 on 2021-06-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='cordinates',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='work_time',
        ),
        migrations.AddField(
            model_name='contact',
            name='from_hour',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='lat',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='lon',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='to_hour',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='weekday',
            field=models.IntegerField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
