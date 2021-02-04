# Generated by Django 3.1.6 on 2021-02-04 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ESEA_core', '0004_auto_20210204_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organisations',
            field=models.ManyToManyField(through='ESEA_core.UserOrganisation', to='ESEA_core.Organisation'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='users',
            field=models.ManyToManyField(through='ESEA_core.UserOrganisation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userorganisation',
            name='organisation',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='organisations', to='ESEA_core.organisation'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='userorganisation',
            unique_together={('user', 'organisation')},
        ),
    ]