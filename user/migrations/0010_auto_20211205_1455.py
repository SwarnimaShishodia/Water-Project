# Generated by Django 3.1.7 on 2021-12-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_subscribe_mobno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='planowner',
            field=models.CharField(max_length=50),
        ),
    ]
