# Generated by Django 5.1.1 on 2024-10-28 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_alter_plant_created_at_alter_plant_maximun_humidity_and_more'),
        ('smartpots', '0002_rename_ligth_level_sensorsdata_light_level'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartpot',
            name='size',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='smartpot',
            name='status',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smartpots', to='plants.plant'),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='pot_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='ubication',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smartpots', to='users.userprofile'),
        ),
    ]
