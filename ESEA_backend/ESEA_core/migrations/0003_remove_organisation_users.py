# Generated by Django 3.1.6 on 2021-02-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ESEA_core', '0002_auto_20210204_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='users',
        ),
    ]
