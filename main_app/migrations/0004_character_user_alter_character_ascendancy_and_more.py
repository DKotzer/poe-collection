# Generated by Django 4.0.3 on 2022-04-01 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_character_ascendancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='ascendancy',
            field=models.CharField(choices=[('https://poe.ninja/images/classes/Slayer_avatar.png', 'Slayer'), ('https://poe.ninja/images/classes/Gladiator_avatar.png', 'Gladiator'), ('https://poe.ninja/images/classes/Champion_avatar.png', 'Champion'), ('https://poe.ninja/images/classes/Assassin _avatar.png', 'Assassin '), ('https://poe.ninja/images/classes/Saboteur _avatar.png', 'Saboteur '), ('https://poe.ninja/images/classes/Trickster_avatar.png', 'Trickster'), ('https://poe.ninja/images/classes/Juggernaut _avatar.png', 'Juggernaut '), ('https://poe.ninja/images/classes/Berserker _avatar.png', 'Berserker '), ('https://poe.ninja/images/classes/Chieftain _avatar.png', 'Chieftain '), ('https://poe.ninja/images/classes/Necromancer _avatar.png', 'Necromancer '), ('https://poe.ninja/images/classes/Elementalist _avatar.png', 'Elementalist '), ('https://poe.ninja/images/classes/Occultist _avatar.png', 'Occultist '), ('https://poe.ninja/images/classes/Deadeye_avatar.png', 'Deadeye'), ('https://poe.ninja/images/classes/Raider_avatar.png', 'Raider'), ('https://poe.ninja/images/classes/Pathfinder_avatar.png', 'Pathfinder'), ('https://poe.ninja/images/classes/Inquisitor_avatar.png', 'Inquisitor'), ('https://poe.ninja/images/classes/Hierophant_avatar.png', 'Hierophant'), ('https://poe.ninja/images/classes/Guardian_avatar.png', 'Guardian'), ('https://poe.ninja/images/classes/Ascendant_avatar.png', 'Ascendant')], default='Slayer', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_slot',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
