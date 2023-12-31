# Generated by Django 4.2.7 on 2023-11-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0003_booked_delete_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(verbose_name=0)),
                ('phone', models.IntegerField(max_length=15)),
                ('classes', models.CharField(default='Aerobics', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
    ]
