# Generated by Django 5.0.6 on 2024-06-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos', '0008_alter_user_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='correo_electronico',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]