# Generated by Django 2.1.7 on 2019-04-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20190413_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
