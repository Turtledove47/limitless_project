# Generated by Django 4.2.3 on 2023-07-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_alter_operator_caa_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='user',
            new_name='owner',
        ),
    ]