# Generated by Django 2.1.4 on 2019-03-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='flat_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adress',
            name='house_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='tel_number',
            field=models.IntegerField(),
        ),
    ]
