# Generated by Django 4.1.7 on 2023-04-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_clip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uclip_map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quartier', models.CharField(max_length=250)),
                ('Localite', models.CharField(max_length=250)),
                ('Latitude', models.IntegerField()),
                ('Longitude', models.IntegerField()),
                ('Html', models.FileField(upload_to='Files')),
            ],
        ),
        migrations.DeleteModel(
            name='map',
        ),
    ]
