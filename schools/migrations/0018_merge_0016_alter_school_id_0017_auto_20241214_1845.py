# Generated by Django 5.0.1 on 2024-12-14 18:50

from django.db import migrations, models
import uuid

BATCH_SIZE = 1000

def generate_uuid(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    total_records = School.objects.count()
    for start in range(0, total_records, BATCH_SIZE):
        end = min(start + BATCH_SIZE, total_records)
        for school in School.objects.all()[start:end]:
            school.new_id = uuid.uuid4()
            school.save()

class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0016_alter_school_id'),
        ('schools', '0017_auto_20241214_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='new_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(generate_uuid),
        migrations.AlterField(
            model_name='school',
            name='new_id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
        ),
        migrations.RemoveField(
            model_name='school',
            name='id',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='new_id',
            new_name='id',
        ),
    ]