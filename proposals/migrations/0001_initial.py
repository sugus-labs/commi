# Generated by Django 4.2.1 on 2023-06-13 19:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier', primary_key=True, serialize=False, verbose_name='UUID')),
                ('title', models.CharField(help_text='The main title identifier of the proposal', max_length=500, verbose_name='title')),
                ('content', models.TextField(help_text='The explanation of the proposal', verbose_name='content')),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text='The date of creation', verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, help_text='The date of the last modification', verbose_name='modification date')),
                ('deletion_date', models.DateTimeField(help_text='The date of deletion', verbose_name='deletion date')),
            ],
        ),
    ]
