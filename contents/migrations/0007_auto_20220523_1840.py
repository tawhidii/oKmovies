# Generated by Django 3.2 on 2022-05-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_auto_20220523_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='season_title',
        ),
        migrations.AddField(
            model_name='season',
            name='season_title_or_number',
            field=models.CharField(default=None, max_length=150, unique=True, verbose_name='Season title or number'),
            preserve_default=False,
        ),
    ]
