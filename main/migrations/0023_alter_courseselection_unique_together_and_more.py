# Generated by Django 4.1 on 2022-08-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_majorcourse_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseselection',
            unique_together={('student', 'section')},
        ),
        migrations.AlterUniqueTogether(
            name='instructorcourse',
            unique_together={('course', 'instructor')},
        ),
        migrations.AlterUniqueTogether(
            name='majorinstructor',
            unique_together={('major', 'instructor')},
        ),
    ]
