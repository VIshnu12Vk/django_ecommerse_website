# Generated by Django 4.2.4 on 2023-09-13 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user_phone',
        ),
    ]
