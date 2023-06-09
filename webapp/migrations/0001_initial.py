# Generated by Django 4.2.1 on 2023-06-01 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caquita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
                ('dni', models.CharField(blank=True, max_length=100)),
                ('edad', models.IntegerField(blank=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('responables', models.CharField(blank=True, max_length=200)),
                ('motivo_consulta', models.CharField(blank=True, max_length=200)),
                ('derivado', models.BooleanField(default=False)),
                ('telefono', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo'), ('alta', 'alta'), ('derivado', 'derivado')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('asistio', models.BooleanField(default=False)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('monto', models.IntegerField(blank=True, null=True)),
                ('motivo', models.CharField(choices=[('consulta', 'consulta'), ('informe', 'informe'), ('psicotecnico', 'psicotecnico'), ('peritaje', 'peritaje'), ('apto', 'apto')], default='consulta', max_length=20)),
                ('estado', models.CharField(choices=[('pendiente', 'pendiente'), ('saldado', 'saldado')], default='pendiente', max_length=20)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('detalle', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='historiaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True)),
                ('detalle', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='evolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('detalle', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='derivacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('motivo', models.TextField(blank=True)),
                ('detalle', models.TextField(blank=True)),
                ('profesional', models.CharField(blank=True, max_length=200)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente')),
            ],
        ),
    ]
