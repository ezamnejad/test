# Generated by Django 3.0.7 on 2020-06-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200617_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='text',
            field=models.CharField(max_length=70),
        ),
    ]
