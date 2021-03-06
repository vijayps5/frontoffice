# Generated by Django 3.1 on 2020-08-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='getRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('no_of_beds', models.IntegerField()),
                ('room_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('extra_bed_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('room_category', models.IntegerField()),
                ('room_size', models.IntegerField()),
                ('capacity_adults', models.IntegerField()),
                ('capacity_infants', models.IntegerField()),
                ('room_facilties', models.CharField(max_length=100)),
            ],
        ),
    ]
