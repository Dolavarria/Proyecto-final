# Generated by Django 5.0.6 on 2024-05-25 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos', '0003_alter_region_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
