# Generated by Django 4.1 on 2022-08-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manager', models.CharField(max_length=30)),
                ('established_year', models.DateField()),
            ],
        ),
    ]
