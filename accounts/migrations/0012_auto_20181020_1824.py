# Generated by Django 2.1.2 on 2018-10-20 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20181020_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contractor_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.ContractorInformation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='property_owner_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.PropertyOwnerInformation'),
        ),
    ]
