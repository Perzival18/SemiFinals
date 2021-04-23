# Generated by Django 3.2 on 2021-04-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('barangay', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('houseNo', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dateOfBirth', models.CharField(max_length=100)),
                ('vaccineName', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='directory/images')),
            ],
        ),
    ]
