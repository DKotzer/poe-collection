# Generated by Django 4.0.3 on 2022-03-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_item_character_character_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='amulet',
            field=models.CharField(blank=True, default='/static/imgs/smallplus.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='character',
            name='ring1',
            field=models.CharField(blank=True, default='/static/imgs/smallplus.png', max_length=255),
        ),
    ]