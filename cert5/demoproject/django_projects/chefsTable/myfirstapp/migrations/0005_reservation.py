# Generated by Django 4.2.4 on 2023-08-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0004_remove_inputform_time_log_inputform_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=300, verbose_name='Phone number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
