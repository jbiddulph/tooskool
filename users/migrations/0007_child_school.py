# Generated by Django 5.0.1 on 2024-12-14 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0016_alter_school_id'),
        ('users', '0006_remove_child_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.school'),
        ),
    ]
