# Generated by Django 5.0.2 on 2024-03-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
