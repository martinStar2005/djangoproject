# Generated by Django 5.0.6 on 2024-05-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='personals/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
