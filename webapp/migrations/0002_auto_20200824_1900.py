# Generated by Django 3.1 on 2020-08-24 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
		migrations.RenameField('getRooms', 'room_no', 'hotel_room_no'),
		migrations.RenameField('getRooms', 'room_name', 'hotel_room_name'),
		migrations.RenameField('getRooms', 'no_of_beds', 'hotel_no_of_beds'),
		migrations.RenameField('getRooms', 'room_price', 'hotel_price'),
		migrations.RenameField('getRooms', 'extra_bed_price', 'hotel_extra_bed_price'),
		migrations.RenameField('getRooms', 'room_category', 'hotel_room_catagory'),
		migrations.RenameField('getRooms', 'room_size', 'hotel_room_size'),
		migrations.RenameField('getRooms', 'capacity_adults', 'hotel_room_no_of_adults'),
		migrations.RenameField('getRooms', 'capacity_infants', 'hotel_room_no_of_childs'),
		migrations.RenameField('getRooms', 'room_facilties', 'hotel_room_facilities')
		
    ]