# Generated by Django 4.0 on 2023-11-10 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jornalistas', '0005_remove_historicoprofissional_contato_da_referencia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencia',
            name='historico_profissional',
        ),
        migrations.DeleteModel(
            name='HistoricoProfissional',
        ),
        migrations.DeleteModel(
            name='Referencia',
        ),
    ]
