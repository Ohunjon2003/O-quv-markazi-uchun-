# Generated by Django 5.0.3 on 2024-05-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='image',
            field=models.ImageField(default='images/user.png', upload_to='profiles'),
        ),
    ]
