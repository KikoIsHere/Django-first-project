# Generated by Django 3.2.4 on 2021-06-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0002_alter_question_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['placement']},
        ),
        migrations.AddField(
            model_name='question',
            name='placement',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
