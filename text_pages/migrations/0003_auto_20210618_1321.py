# Generated by Django 3.2.4 on 2021-06-18 13:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_pages', '0002_textpage_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='textpage',
            name='position',
            field=models.CharField(choices=[('home', 'Home'), ('footer', 'Footer'), ('about_us', 'About Us')], max_length=20),
        ),
    ]