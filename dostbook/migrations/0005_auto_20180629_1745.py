# Generated by Django 2.0.6 on 2018-06-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dostbook', '0004_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='idi',
        ),
        migrations.AlterField(
            model_name='friends',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
