# Generated by Django 3.1.14 on 2022-12-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0004_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]
