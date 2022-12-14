# Generated by Django 4.1 on 2022-09-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_semaster_course_semastes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=4, verbose_name='سال تحصیلی')),
                ('semester', models.CharField(choices=[('1', 'مهر'), ('2', 'بهمن'), ('3', 'تابستان')], max_length=1)),
            ],
            options={
                'verbose_name': 'نیم\u200cسال تحصیلی',
                'verbose_name_plural': 'نیم\u200cسال های تحصیلی',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='semastes',
        ),
        migrations.DeleteModel(
            name='Semaster',
        ),
        migrations.AddField(
            model_name='course',
            name='semestres',
            field=models.ManyToManyField(to='main.semester'),
        ),
    ]
