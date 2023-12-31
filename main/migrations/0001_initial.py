# Generated by Django 4.1.1 on 2023-04-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrehospital', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Hospitales',
                'db_table': 'Hospital',
                'ordering': ['nombrehospital'],
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('institucionid', models.IntegerField(db_column='institucionId', primary_key=True, serialize=False)),
                ('nombreinstitucion', models.CharField(blank=True, db_column='nombreInstitucion', max_length=150, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('departamento', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'db_table': 'Institucion',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idpac', models.AutoField(db_column='idPac', primary_key=True, serialize=False)),
                ('cedulapac', models.IntegerField(blank=True, db_column='cedulaPac', null=True, unique=True, validators=[main.validators.val_cedulapac])),
                ('apellido_materno', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=100, null=True)),
                ('nombreuno', models.CharField(blank=True, db_column='nombreUno', max_length=100, null=True)),
                ('nombredos', models.CharField(blank=True, db_column='nombreDos', max_length=100, null=True)),
                ('fechanac', models.CharField(blank=True, db_column='fechaNac', max_length=100, null=True)),
                ('numgestacion', models.IntegerField(blank=True, db_column='numGestacion', null=True)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'db_table': 'Paciente',
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('idreporte', models.AutoField(db_column='idReporte', primary_key=True, serialize=False)),
                ('efw', models.CharField(blank=True, max_length=100, null=True)),
                ('edb', models.CharField(blank=True, max_length=100, null=True)),
                ('ga', models.CharField(blank=True, max_length=100, null=True)),
                ('csp_1', models.CharField(blank=True, max_length=50, null=True)),
                ('csp_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('cm_1', models.CharField(blank=True, max_length=50, null=True)),
                ('cm_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_1', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_1', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_1', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('va_1', models.CharField(blank=True, max_length=50, null=True)),
                ('va_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('vp_1', models.CharField(blank=True, max_length=50, null=True)),
                ('vp_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('ga_days', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Reportes',
                'db_table': 'Reporte',
            },
        ),
        migrations.CreateModel(
            name='Tipomedicion',
            fields=[
                ('idTipoMedicion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMedicion', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'TiposMedicion',
                'db_table': 'TipoMedicion',
            },
        ),
        migrations.CreateModel(
            name='Usuarioexterno',
            fields=[
                ('cedulaext', models.IntegerField(primary_key=True, serialize=False, validators=[main.validators.val_cedulaext])),
                ('nombresext', models.CharField(blank=True, max_length=150, null=True)),
                ('apellidosext', models.CharField(blank=True, max_length=150, null=True)),
                ('telefonoext', models.CharField(blank=True, max_length=50, null=True)),
                ('direccionext', models.CharField(blank=True, max_length=200, null=True)),
                ('institutionid', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.institucion')),
                ('userid', models.OneToOneField(db_column='UserId', default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UsuariosExternos',
                'db_table': 'UsuarioExterno',
            },
        ),
        migrations.CreateModel(
            name='Personalsalud',
            fields=[
                ('cedulamed', models.IntegerField(primary_key=True, serialize=False)),
                ('nombresmed', models.CharField(max_length=150)),
                ('apellidosmed', models.CharField(max_length=150)),
                ('telefonomed', models.CharField(max_length=50, unique=True)),
                ('direccionmed', models.CharField(max_length=200)),
                ('hospitalid', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.hospital', verbose_name='Hospitales')),
                ('userid', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personal',
                'db_table': 'PersonalSalud',
                'ordering': ['cedulamed'],
            },
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('idmedicion', models.AutoField(db_column='idMedicion', primary_key=True, serialize=False)),
                ('ga', models.IntegerField(db_column='ga')),
                ('valormin', models.FloatField(blank=True, db_column='valorMin', max_length=50, null=True)),
                ('valorinter', models.FloatField(blank=True, db_column='valorMax', max_length=50, null=True)),
                ('valordev', models.FloatField(blank=True, db_column='valorDev', max_length=50, null=True)),
                ('id_tipo_medicion', models.OneToOneField(db_column='idTipoMedicion', on_delete=django.db.models.deletion.CASCADE, to='main.tipomedicion')),
            ],
            options={
                'verbose_name_plural': 'Mediciones',
                'db_table': 'Medicion',
            },
        ),
        migrations.CreateModel(
            name='Historiaclinica',
            fields=[
                ('idhistoriaclinica', models.AutoField(db_column='idHistoriaClinica', primary_key=True, serialize=False)),
                ('antquirurgico', models.TextField(blank=True, db_column='antQuirurgico', null=True)),
                ('antpatologico', models.TextField(blank=True, db_column='antPatologico', null=True)),
                ('antginecologico', models.TextField(blank=True, db_column='antGinecologico', null=True)),
                ('lmp', models.CharField(blank=True, db_column='LMP', max_length=50, null=True)),
                ('idPaciente', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.paciente')),
            ],
            options={
                'verbose_name_plural': 'Historiales',
                'db_table': 'HistoriaClinica',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('consultaid', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_consulta', models.DateTimeField()),
                ('motivo_consulta', models.CharField(default='Ultrasonido de control', max_length=100)),
                ('txtresults', models.CharField(blank=True, max_length=100, null=True)),
                ('medUltrasonido', models.CharField(blank=True, max_length=200, null=True)),
                ('idfeto', models.IntegerField(blank=True, null=True)),
                ('idpac', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.paciente')),
                ('idreporte', models.OneToOneField(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.reporte')),
                ('medConsulta', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.personalsalud')),
            ],
            options={
                'verbose_name_plural': 'Consultas',
                'db_table': 'Consulta',
                'ordering': ['consultaid'],
            },
        ),
    ]
