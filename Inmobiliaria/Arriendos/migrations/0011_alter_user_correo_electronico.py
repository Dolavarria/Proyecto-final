# Generated by Django 5.0.6 on 2024-06-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos', '0010_alter_user_correo_electronico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='correo_electronico',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]