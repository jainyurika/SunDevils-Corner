# Generated by Django 3.1.7 on 2021-03-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
    ]
