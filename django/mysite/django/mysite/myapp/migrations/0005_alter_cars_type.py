# Generated by Django 5.0.4 on 2024-04-25 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_cars_mark_alter_cars_number_alter_cars_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.typecars'),
        ),
    ]
