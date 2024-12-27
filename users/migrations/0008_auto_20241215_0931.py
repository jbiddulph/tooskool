from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_child_school'),  # Replace with your last migration
    ]

    operations = [
        # Alter the `school` field to reference UUIDs
        migrations.AlterField(
            model_name='child',
            name='school',
            field=models.ForeignKey(
                to='schools.school',
                on_delete=models.CASCADE,
                null=True,
                blank=True,
            ),
        ),
    ]
