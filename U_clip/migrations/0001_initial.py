# Generated by Django 4.1.7 on 2023-04-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quartier', models.CharField(max_length=250)),
                ('Localite', models.CharField(max_length=250)),
                ('Latitude', models.IntegerField()),
                ('Longitude', models.IntegerField()),
                ('Photo', models.FileField(upload_to='Files')),
            ],
        ),
    ]
