# Generated by Django 3.1.7 on 2021-03-22 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Grocery Store', 'Grocery Store'), ('Apartment', 'Apartment'), ('Haircut Shop', 'Haircut Shop'), ('Restaurants', 'Restaurants')], max_length=15, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Business Categories',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Title')),
                ('about', models.TextField(max_length=5000, null=True, verbose_name='Description')),
                ('upvotecount', models.IntegerField(default=0, verbose_name='Upvote Count')),
                ('phone', models.CharField(max_length=10, verbose_name='Contact Number')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('website', models.CharField(max_length=100, verbose_name='Website')),
                ('distfromcampus', models.FloatField(default=0, verbose_name='Distance from Campus')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.businesscat', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
    ]