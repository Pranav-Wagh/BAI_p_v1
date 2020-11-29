# Generated by Django 3.1.2 on 2020-10-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0005_auto_20201030_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation', models.ImageField(upload_to='uploads/')),
                ('sanitary', models.ImageField(upload_to='uploads/')),
                ('school', models.ImageField(blank=True, upload_to='uploads/')),
                ('polution_measures', models.ImageField(upload_to='uploads/')),
                ('ISO_accreditation', models.CharField(blank=True, choices=[('on', 'on'), ('off', 'off')], max_length=4)),
                ('conseravation_A', models.TextField(max_length=200)),
                ('conseravation_B', models.TextField(max_length=200)),
                ('renewable_energy_text', models.TextField(blank=True, max_length=200)),
                ('renewable_energy_pic', models.FileField(blank=True, upload_to='uploads/')),
                ('green_building', models.TextField(blank=True, max_length=2000)),
                ('debris_management', models.TextField(blank=True, max_length=2000)),
                ('seminars', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='SafetynWellfare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitered', models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4)),
                ('bywhom', models.TextField(blank=True, max_length=200)),
                ('measures', models.TextField(max_length=2000)),
                ('medical_aid', models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4)),
                ('incidents', models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4)),
                ('safety_audits', models.FileField(blank=True, upload_to='uploads/')),
            ],
        ),
    ]
