# Generated by Django 4.1.1 on 2022-11-08 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('locations', models.CharField(choices=[('H', 'Home'), ('C', 'Cafe'), ('R', 'Restaurant'), ('F', 'Friends House')], default='H', max_length=1)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coffee')),
            ],
        ),
    ]
