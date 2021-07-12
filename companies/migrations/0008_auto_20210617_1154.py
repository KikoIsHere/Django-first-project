# Generated by Django 3.2.4 on 2021-06-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_agreement_right'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='right',
            name='company',
        ),
        migrations.AlterModelOptions(
            name='companie',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='companie',
            name='placement',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companie',
            name='meta_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='companie',
            name='meta_keywords',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Agreement',
        ),
        migrations.DeleteModel(
            name='Right',
        ),
    ]
