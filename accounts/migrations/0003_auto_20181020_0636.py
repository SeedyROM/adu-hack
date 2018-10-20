# Generated by Django 2.1.2 on 2018-10-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0004_auto_20181020_0636'),
        ('accounts', '0002_contractorinformation_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorinformation',
            name='reviews',
            field=models.ManyToManyField(to='connections.Review'),
        ),
        migrations.AddField(
            model_name='propertyownerinformation',
            name='reviews',
            field=models.ManyToManyField(to='connections.Review'),
        ),
    ]