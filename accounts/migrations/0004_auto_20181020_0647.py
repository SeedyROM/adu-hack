# Generated by Django 2.1.2 on 2018-10-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181020_0636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractorinformation',
            options={'verbose_name_plural': 'Contractors'},
        ),
        migrations.AlterModelOptions(
            name='propertyownerinformation',
            options={'verbose_name_plural': 'Property Owners'},
        ),
        migrations.AlterField(
            model_name='contractorinformation',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='connections.Review'),
        ),
    ]