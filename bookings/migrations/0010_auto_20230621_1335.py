# Generated by Django 3.2.2 on 2023-06-21 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='The date of creation', verbose_name='creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='deletion_date',
            field=models.DateTimeField(blank=True, help_text='The date of deletion', null=True, verbose_name='deletion date'),
        ),
        migrations.AddField(
            model_name='profile',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, help_text='The date of the last modification', verbose_name='modification date'),
        ),
    ]