# Generated by Django 3.0.8 on 2020-08-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_podcast_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='logo',
            field=models.ImageField(default='../media/default.jpg', upload_to='../media/Pod_Logo'),
        ),
    ]
