# Generated by Django 3.2 on 2022-07-06 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0014_alter_contentgallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TvSeriesGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_image', models.ImageField(upload_to='tv-series/%Y/%m/%d/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.content')),
            ],
            options={
                'verbose_name': 'Tv Series Gallery',
                'verbose_name_plural': 'Tv Series Gallery',
            },
        ),
    ]
