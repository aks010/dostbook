# Generated by Django 2.0.6 on 2018-07-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dostbook', '0010_auto_20180705_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='profpic',
            name='status',
            field=models.IntegerField(default='1'),
        ),
    ]
