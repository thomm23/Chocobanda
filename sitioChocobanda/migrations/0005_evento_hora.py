# Generated by Django 5.1 on 2025-01-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioChocobanda', '0004_ajustespagina_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='hora',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
