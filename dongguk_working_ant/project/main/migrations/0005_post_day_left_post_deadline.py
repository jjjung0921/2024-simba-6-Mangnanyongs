# Generated by Django 5.0.6 on 2024-06-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_post_building_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='day_left',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
