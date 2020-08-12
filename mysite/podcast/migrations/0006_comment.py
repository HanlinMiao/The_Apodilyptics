# Generated by Django 3.0.8 on 2020-08-12 20:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20200812_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='podcast.podcast')),
            ],
        ),
    ]