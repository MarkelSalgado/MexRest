# Generated by Django 4.1.1 on 2022-10-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platerak', '0003_alter_platerak_prezioa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platerak',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
