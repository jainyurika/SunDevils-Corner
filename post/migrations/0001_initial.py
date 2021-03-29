# Generated by Django 3.1.7 on 2021-03-22 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(max_length=5000, null=True, verbose_name='Description')),
                ('upvotecount', models.IntegerField(default=0, verbose_name='Upvote Count')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Post Created On')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000, null=True, verbose_name='Description')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
