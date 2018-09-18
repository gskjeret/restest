# Generated by Django 2.1.1 on 2018-09-18 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DebugMessages',
            fields=[
                ('line_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'debug_messages',
            },
        ),
        migrations.CreateModel(
            name='Faktura',
            fields=[
                ('faktura_id', models.AutoField(primary_key=True, serialize=False)),
                ('faktura_dato', models.DateTimeField(blank=True, null=True)),
                ('frist_dato', models.DateField(blank=True, null=True)),
                ('belop_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mva_belop', models.DecimalField(decimal_places=2, max_digits=7)),
                ('totalbelop', models.DecimalField(decimal_places=2, max_digits=7)),
                ('notat', models.CharField(blank=True, max_length=2000, null=True)),
                ('kidnr', models.CharField(blank=True, max_length=30, null=True)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'faktura',
            },
        ),
        migrations.CreateModel(
            name='Fakturalinje',
            fields=[
                ('fakturalinje_id', models.AutoField(primary_key=True, serialize=False)),
                ('linjenr', models.PositiveIntegerField()),
                ('antall', models.PositiveIntegerField()),
                ('rabatt_pros', models.PositiveIntegerField()),
                ('belop_linje_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('kommentar', models.CharField(blank=True, max_length=200, null=True)),
                ('faktura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Faktura')),
            ],
            options={
                'db_table': 'fakturalinje',
            },
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('kunde_id', models.AutoField(primary_key=True, serialize=False)),
                ('kundenavn', models.CharField(max_length=80)),
                ('adresse', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefonnr', models.CharField(blank=True, max_length=20, null=True)),
                ('kontaktperson', models.CharField(blank=True, max_length=60, null=True)),
                ('telefonnr1', models.CharField(blank=True, max_length=20, null=True)),
                ('kontaktperson2', models.CharField(blank=True, max_length=60, null=True)),
                ('telefonnr2', models.CharField(blank=True, max_length=20, null=True)),
                ('emailadresse', models.CharField(blank=True, max_length=200, null=True)),
                ('merknader', models.CharField(blank=True, max_length=2000, null=True)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'kunde',
            },
        ),
        migrations.CreateModel(
            name='Kundetype',
            fields=[
                ('kundetype_kode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('beskrivelse', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'kundetype',
            },
        ),
        migrations.CreateModel(
            name='Leverandor',
            fields=[
                ('leverandor_id', models.AutoField(primary_key=True, serialize=False)),
                ('leverandornavn', models.CharField(max_length=80)),
                ('leverandorkode', models.CharField(max_length=5)),
                ('organisasjonsnr', models.CharField(blank=True, max_length=15, null=True)),
                ('besoksadresse', models.CharField(blank=True, max_length=1000, null=True)),
                ('postadresse', models.CharField(blank=True, max_length=1000, null=True)),
                ('kontaktperson1', models.CharField(blank=True, max_length=60, null=True)),
                ('telefonnr1', models.CharField(blank=True, max_length=20, null=True)),
                ('kontaktperson2', models.CharField(blank=True, max_length=60, null=True)),
                ('telefonnr2', models.CharField(blank=True, max_length=20, null=True)),
                ('emailadresse', models.CharField(blank=True, max_length=200, null=True)),
                ('hjemmeside', models.CharField(blank=True, max_length=200, null=True)),
                ('merknader', models.CharField(blank=True, max_length=2000, null=True)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'leverandor',
            },
        ),
        migrations.CreateModel(
            name='Ordre',
            fields=[
                ('ordre_id', models.AutoField(primary_key=True, serialize=False)),
                ('ordre_dato', models.DateTimeField()),
                ('belop_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mva_belop', models.DecimalField(decimal_places=2, max_digits=7)),
                ('totalbelop', models.DecimalField(decimal_places=2, max_digits=7)),
                ('notat', models.CharField(blank=True, max_length=2000, null=True)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('kunde', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Kunde')),
            ],
            options={
                'db_table': 'ordre',
            },
        ),
        migrations.CreateModel(
            name='Ordrelinje',
            fields=[
                ('ordrelinje_id', models.AutoField(primary_key=True, serialize=False)),
                ('linjenr', models.PositiveIntegerField()),
                ('antall', models.PositiveIntegerField()),
                ('rabatt_pros', models.PositiveIntegerField()),
                ('belop_linje_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('kommentar', models.CharField(blank=True, max_length=200, null=True)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('ordre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Ordre')),
            ],
            options={
                'db_table': 'ordrelinje',
            },
        ),
        migrations.CreateModel(
            name='Ordrestatus',
            fields=[
                ('statuskode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('beskrivelse', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ordrestatus',
            },
        ),
        migrations.CreateModel(
            name='Vare',
            fields=[
                ('produkt_id', models.AutoField(primary_key=True, serialize=False)),
                ('produktkode', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('produktnavn', models.CharField(max_length=80)),
                ('beskrivelse', models.CharField(blank=True, max_length=4000, null=True)),
                ('pris_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('beholdning', models.PositiveIntegerField()),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('leverandor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Leverandor')),
            ],
            options={
                'db_table': 'vare',
            },
        ),
        migrations.CreateModel(
            name='Varepris',
            fields=[
                ('varepris_id', models.AutoField(primary_key=True, serialize=False)),
                ('pris_fra_dato', models.DateField()),
                ('pris_u_mva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('reg_dato', models.DateTimeField(blank=True, null=True)),
                ('reg_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('endret_dato', models.DateTimeField(blank=True, null=True)),
                ('endret_bruker', models.CharField(blank=True, max_length=20, null=True)),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Vare')),
            ],
            options={
                'db_table': 'varepris',
            },
        ),
        migrations.AddField(
            model_name='ordrelinje',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Vare'),
        ),
        migrations.AddField(
            model_name='ordre',
            name='status',
            field=models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Ordrestatus'),
        ),
        migrations.AddField(
            model_name='kunde',
            name='kundetype',
            field=models.ForeignKey(blank=True, db_column='kundetype', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Kundetype'),
        ),
        migrations.AddField(
            model_name='fakturalinje',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Vare'),
        ),
        migrations.AddField(
            model_name='faktura',
            name='ordre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Ordre'),
        ),
        migrations.AlterUniqueTogether(
            name='varepris',
            unique_together={('produkt', 'pris_fra_dato')},
        ),
        migrations.AlterUniqueTogether(
            name='ordrelinje',
            unique_together={('ordre', 'linjenr')},
        ),
        migrations.AlterUniqueTogether(
            name='fakturalinje',
            unique_together={('faktura', 'linjenr')},
        ),
    ]
