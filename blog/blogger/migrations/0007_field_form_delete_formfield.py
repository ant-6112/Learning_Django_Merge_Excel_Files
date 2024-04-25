# Generated by Django 4.2.11 on 2024-04-25 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='blogger.form'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
    ]
