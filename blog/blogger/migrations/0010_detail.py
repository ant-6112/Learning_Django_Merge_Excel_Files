# Generated by Django 4.2.11 on 2024-04-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0009_remove_field_form_field_projectform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
            ],
        ),
    ]
