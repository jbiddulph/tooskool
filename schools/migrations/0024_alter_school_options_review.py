# Generated by Django 5.0.1 on 2024-12-21 10:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0023_alter_school_id'),
        ('users', '0009_alter_child_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['establishment_name']},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
            options={
                'ordering': ['-created'],
                'unique_together': {('parent', 'school')},
            },
        ),
    ]
