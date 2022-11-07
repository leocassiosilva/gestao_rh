# Generated by Django 3.1.14 on 2022-11-07 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('registro_hora_extra', '0002_auto_20221107_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrohoraextra',
            name='pertence',
        ),
        migrations.AddField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]