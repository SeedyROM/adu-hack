# Generated by Django 2.1.2 on 2018-10-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_auto_20181020_0625'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorinformation',
            name='services',
            field=models.ManyToManyField(to='connections.Service'),
        ),
    ]
