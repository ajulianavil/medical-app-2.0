# Generated by Django 4.1.7 on 2023-06-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_consulta_idfeto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='txtresults',
        ),
        migrations.AddField(
            model_name='reporte',
            name='txtresults',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
