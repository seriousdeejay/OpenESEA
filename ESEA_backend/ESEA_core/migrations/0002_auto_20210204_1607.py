# Generated by Django 3.1.6 on 2021-02-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESEA_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
