# Generated by Django 3.1 on 2022-03-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diadiem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diadiem',
            name='hinh_cover',
            field=models.ImageField(blank=True, upload_to='photos/diadiem'),
        ),
    ]
