# Generated by Django 3.2.2 on 2023-06-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_schedule_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='comments',
            field=models.TextField(blank=True, help_text='The comments of the booking if exists', max_length=5000, null=True, verbose_name='comments'),
        ),
    ]
