# Generated by Django 4.1.1 on 2023-06-08 17:25

from django.db import migrations, models
import django.db.models.deletion
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_feto_posicion_feto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsalud',
            name='cedulamed',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[main.validators.val_cedulamed, main.validators.validate_unique_user_identification]),
        ),
        migrations.AlterField(
            model_name='personalsalud',
            name='telefonomed',
            field=models.CharField(max_length=50, unique=True, validators=[main.validators.validate_unique_phone]),
        ),
        migrations.AlterField(
            model_name='usuarioexterno',
            name='cedulaext',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[main.validators.val_cedulaext, main.validators.validate_unique_user_identification]),
        ),
        migrations.AlterField(
            model_name='usuarioexterno',
            name='telefonoext',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[main.validators.validate_unique_phone]),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('idimage', models.BigAutoField(primary_key=True, serialize=False)),
                ('image_data', models.BinaryField()),
                ('reporte', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.reporte')),
            ],
        ),
    ]
