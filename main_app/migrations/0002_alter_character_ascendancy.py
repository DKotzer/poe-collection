# Generated by Django 4.0.3 on 2022-03-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='ascendancy',
            field=models.CharField(choices=[('Slayer', 'https://poe.ninja/images/classes/Slayer_avatar.png'), ('Gladiator', 'https://poe.ninja/images/classes/Gladiator_avatar.png')], default='https://poe.ninja/images/classes/Slayer_avatar.png', max_length=100),
        ),
    ]