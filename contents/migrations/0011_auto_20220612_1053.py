# Generated by Django 3.2 on 2022-06-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_auto_20220612_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='cover_photos',
            field=models.ImageField(null=True, upload_to='uploads/movies/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='cover_photos',
            field=models.ImageField(null=True, upload_to='uploads/movies/% Y/% m/% d/'),
        ),
    ]