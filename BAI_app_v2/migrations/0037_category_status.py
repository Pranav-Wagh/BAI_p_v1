# Generated by Django 3.1.2 on 2020-12-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0036_project_info_1_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('none', 'none'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='none', max_length=20),
        ),
    ]