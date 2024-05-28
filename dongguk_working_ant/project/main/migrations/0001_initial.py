# Generated by Django 5.0.6 on 2024-05-28 00:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50, null=True)),
                ('is_attending', models.IntegerField()),
                ('department', models.CharField(max_length=50, null=True)),
                ('place', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('day', models.TextField(max_length=50)),
                ('time', models.TextField(max_length=50)),
                ('recruitment', models.IntegerField(default=0, null=True)),
                ('wage', models.IntegerField(default=0, null=True)),
                ('deadline', models.DateField(null=True)),
                ('body', models.TextField()),
                ('is_income_bracket', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('pub_date', models.DateTimeField()),
                ('scrap', models.ManyToManyField(blank=True, related_name='scraped', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
