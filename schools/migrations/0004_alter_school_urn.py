# Generated by Django 5.0.1 on 2024-12-12 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_rename_ofstead_special_measures_school_ofsted_special_measures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='urn',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
