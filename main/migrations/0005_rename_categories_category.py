# Generated by Django 5.1.3 on 2025-01-07 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_author_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
