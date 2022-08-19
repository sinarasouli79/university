# Generated by Django 4.1 on 2022-08-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_major_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.faculty'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.major')),
            ],
        ),
    ]
