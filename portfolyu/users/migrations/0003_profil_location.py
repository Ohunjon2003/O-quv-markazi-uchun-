# Generated by Django 5.0.3 on 2024-05-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profil_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]