# Generated by Django 4.1.7 on 2023-08-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logindata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('pswd', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('pswd', models.CharField(max_length=12)),
            ],
        ),
    ]