# Generated by Django 3.1.2 on 2020-11-08 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20201028_2325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Categories',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='Categories',
        ),
    ]