# Generated by Django 3.1.2 on 2020-10-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0010_auto_20201030_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others',
            name='accomodation',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='others',
            name='polution_measures',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='others',
            name='sanitary',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='safetynwellfare',
            name='bywhom',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='safetynwellfare',
            name='incidents',
            field=models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4),
        ),
        migrations.AlterField(
            model_name='safetynwellfare',
            name='medical_aid',
            field=models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4),
        ),
        migrations.AlterField(
            model_name='safetynwellfare',
            name='monitered',
            field=models.CharField(choices=[('on', 'on'), ('off', 'off')], max_length=4),
        ),
    ]
