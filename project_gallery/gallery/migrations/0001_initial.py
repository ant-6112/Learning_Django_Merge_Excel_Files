# Generated by Django 4.2.11 on 2024-06-11 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project_id', models.CharField(editable=False, max_length=22, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('programmed_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=200)),
                ('field_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('email', 'Email'), ('date', 'Date')], max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='gallery.project')),
            ],
        ),
    ]