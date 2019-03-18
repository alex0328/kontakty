# Generated by Django 2.1.4 on 2019-03-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190317_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email_type',
            field=models.IntegerField(choices=[(1, 'Domowy'), (2, 'Praca'), (3, 'Inny')], default=1),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='tel_type',
            field=models.IntegerField(choices=[(1, 'Domowy'), (2, 'Kom'), (3, 'Praca'), (4, 'Inny')], default=1),
        ),
    ]
