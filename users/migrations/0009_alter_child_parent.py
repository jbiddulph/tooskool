# Generated by Django 5.0.1 on 2024-12-15 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20241215_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='users.profile'),
        ),
    ]
