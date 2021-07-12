# Generated by Django 3.2.4 on 2021-06-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210617_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='weekday',
            new_name='from_weekday',
        ),
        migrations.AddField(
            model_name='contact',
            name='to_weekday',
            field=models.IntegerField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], default=None, unique=True),
            preserve_default=False,
        ),
    ]
