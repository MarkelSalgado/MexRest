# Generated by Django 4.1.1 on 2022-09-28 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platerak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platerak',
            name='izena',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
