# Generated by Django 3.2.9 on 2021-12-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0003_alter_student_assignment_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
