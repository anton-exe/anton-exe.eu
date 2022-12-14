# Generated by Django 4.0.6 on 2022-09-15 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('url_path', models.CharField(blank=True, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TextPageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.textpage')),
            ],
        ),
    ]
