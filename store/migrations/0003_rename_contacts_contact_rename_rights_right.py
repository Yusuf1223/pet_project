# Generated by Django 4.1.3 on 2023-01-19 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_feedback_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
        migrations.RenameModel(
            old_name='Rights',
            new_name='Right',
        ),
    ]
