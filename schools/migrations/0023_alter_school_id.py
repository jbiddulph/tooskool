# Generated by Django 5.0.1 on 2024-12-15 10:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0022_merge_20241214_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
