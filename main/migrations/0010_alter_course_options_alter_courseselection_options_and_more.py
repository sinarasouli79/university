# Generated by Django 4.1 on 2022-08-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_courseselection_section_courseselection_section_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'درس', 'verbose_name_plural': 'درس\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='courseselection',
            options={'verbose_name': 'انتخاب واحد', 'verbose_name_plural': 'انتخاب واحد'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'دانشکده', 'verbose_name_plural': 'دانشکده\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'مدرس', 'verbose_name_plural': 'مدرس\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='instructorcourse',
            options={'verbose_name': 'درس ارائه شده', 'verbose_name_plural': 'درس های ارائه شده'},
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'verbose_name': 'رشته', 'verbose_name_plural': 'رشته\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='majorcourse',
            options={'verbose_name': 'درس های رشته', 'verbose_name_plural': 'درس های رشته\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='majorinstructor',
            options={'verbose_name': 'مدرس های رشته', 'verbose_name_plural': 'مدرس های رشته\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'سکشن', 'verbose_name_plural': 'سکشن\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'دانشجو', 'verbose_name_plural': 'دانشجویان'},
        ),
        migrations.AddField(
            model_name='major',
            name='area_of_interest',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='major',
            name='grade',
            field=models.CharField(choices=[('B', 'کارشناسی'), ('M', 'کارشناسی ارشد'), ('D', 'دکترا')], default='B', max_length=1),
        ),
    ]