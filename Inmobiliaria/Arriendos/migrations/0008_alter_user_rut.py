# Generated by Django 5.0.6 on 2024-06-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos', '0007_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=12),
        ),
    ]