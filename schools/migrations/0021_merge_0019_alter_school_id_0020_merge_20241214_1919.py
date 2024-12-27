import uuid
from django.db import migrations, models

def generate_uuid(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    for school in School.objects.all():
        school.new_id = uuid.uuid4()
        school.save()

class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0018_merge_0016_alter_school_id_0017_auto_20241214_1845'),
    ]

    operations = [
        # Step 1: Add a new UUID column
        migrations.AddField(
            model_name='school',
            name='new_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        # Step 2: Populate the new_id column
        migrations.RunPython(generate_uuid),
        # Step 3: Remove the primary key from the old id column
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.IntegerField(editable=False, null=True),
        ),
        # Step 4: Rename new_id to id and make it the primary key
        migrations.RenameField(
            model_name='school',
            old_name='new_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False),
        ),
        # Step 5: Drop the old id column
        migrations.RemoveField(
            model_name='school',
            name='id',
        ),
    ]