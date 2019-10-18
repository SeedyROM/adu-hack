# Generated by Django 2.1.2 on 2018-10-20 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('connections', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyownerinformation',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='connections.Review'),
        ),
        migrations.AddField(
            model_name='contractorinformation',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='connections.Review'),
        ),
        migrations.AddField(
            model_name='contractorinformation',
            name='services',
            field=models.ManyToManyField(to='connections.Service'),
        ),
        migrations.AddField(
            model_name='user',
            name='contractor_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.ContractorInformation'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='property_owner_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.PropertyOwnerInformation'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]