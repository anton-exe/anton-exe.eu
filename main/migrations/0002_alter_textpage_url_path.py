# Generated by Django 4.0.6 on 2022-09-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='url_path',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]