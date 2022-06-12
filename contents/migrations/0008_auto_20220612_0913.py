# Generated by Django 3.2 on 2022-06-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20220523_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='country',
            field=models.ManyToManyField(related_name='country', to='contents.Country'),
        ),
        migrations.AlterField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='contents.Genre'),
        ),
    ]