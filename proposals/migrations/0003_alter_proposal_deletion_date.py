# Generated by Django 4.2.1 on 2023-06-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_proposal_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='deletion_date',
            field=models.DateTimeField(blank=True, help_text='The date of deletion', null=True, verbose_name='deletion date'),
        ),
    ]
