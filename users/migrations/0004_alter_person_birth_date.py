# Generated by Django 3.2.9 on 2022-01-04 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.date(2004, 1, 9)),
        ),
    ]
