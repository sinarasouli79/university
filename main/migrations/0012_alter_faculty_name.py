# Generated by Django 4.1 on 2022-08-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_instructor_course_remove_instructor_major_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='نام'),
        ),
    ]
