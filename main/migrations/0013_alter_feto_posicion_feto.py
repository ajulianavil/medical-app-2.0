# Generated by Django 4.1.7 on 2023-06-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_consulta_txtresults_reporte_txtresults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feto',
            name='posicion_feto',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
