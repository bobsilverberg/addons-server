# Generated by Django 2.2.12 on 2020-06-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0011_auto_20200610_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addon',
            name='public_stats',
        ),
    ]
