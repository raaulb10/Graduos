# Generated by Django 3.2.9 on 2021-12-22 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('files', '0002_alter_file_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course'),
        ),
    ]
