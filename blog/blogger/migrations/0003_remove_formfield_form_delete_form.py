# Generated by Django 4.2.11 on 2024-04-23 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_form_formfield_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='form',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
