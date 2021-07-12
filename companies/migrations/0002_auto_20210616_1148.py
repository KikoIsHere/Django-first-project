# Generated by Django 3.2.4 on 2021-06-16 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companies',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companies',
            name='title',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('upload', models.FileField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companies')),
            ],
        ),
    ]