# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DebugMessages(models.Model):
    line_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'debug_messages'


class Faktura(models.Model):
    faktura_id = models.AutoField(primary_key=True)
    ordre = models.ForeignKey('Ordre', models.DO_NOTHING)
    faktura_dato = models.DateTimeField(blank=True, null=True)
    frist_dato = models.DateField(blank=True, null=True)
    belop_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    mva_belop = models.DecimalField(max_digits=7, decimal_places=2)
    totalbelop = models.DecimalField(max_digits=7, decimal_places=2)
    notat = models.CharField(max_length=2000, blank=True, null=True)
    kidnr = models.CharField(max_length=30, blank=True, null=True)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'faktura'


class Fakturalinje(models.Model):
    fakturalinje_id = models.AutoField(primary_key=True, serialize=False)
    faktura = models.ForeignKey(Faktura, models.DO_NOTHING)
    linjenr = models.PositiveIntegerField()
    produkt = models.ForeignKey('Vare', models.DO_NOTHING)
    antall = models.PositiveIntegerField()
    rabatt_pros = models.PositiveIntegerField()
    belop_linje_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    kommentar = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'fakturalinje'
        unique_together = (('faktura', 'linjenr'),)


class Kunde(models.Model):
    kunde_id = models.AutoField(primary_key=True)
    kundetype = models.ForeignKey('Kundetype', models.DO_NOTHING, db_column='kundetype', blank=True, null=True)
    kundenavn = models.CharField(max_length=80)
    adresse = models.CharField(max_length=1000, blank=True, null=True)
    telefonnr = models.CharField(max_length=20, blank=True, null=True)
    kontaktperson = models.CharField(max_length=60, blank=True, null=True)
    telefonnr1 = models.CharField(max_length=20, blank=True, null=True)
    kontaktperson2 = models.CharField(max_length=60, blank=True, null=True)
    telefonnr2 = models.CharField(max_length=20, blank=True, null=True)
    emailadresse = models.CharField(max_length=200, blank=True, null=True)
    merknader = models.CharField(max_length=2000, blank=True, null=True)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'kunde'


class Kundetype(models.Model):
    kundetype_kode = models.CharField(primary_key=True, max_length=10)
    beskrivelse = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'kundetype'


class Leverandor(models.Model):
    leverandor_id = models.AutoField(primary_key=True)
    leverandornavn = models.CharField(max_length=80)
    leverandorkode = models.CharField(max_length=5)
    organisasjonsnr = models.CharField(max_length=15, blank=True, null=True)
    besoksadresse = models.CharField(max_length=1000, blank=True, null=True)
    postadresse = models.CharField(max_length=1000, blank=True, null=True)
    kontaktperson1 = models.CharField(max_length=60, blank=True, null=True)
    telefonnr1 = models.CharField(max_length=20, blank=True, null=True)
    kontaktperson2 = models.CharField(max_length=60, blank=True, null=True)
    telefonnr2 = models.CharField(max_length=20, blank=True, null=True)
    emailadresse = models.CharField(max_length=200, blank=True, null=True)
    hjemmeside = models.CharField(max_length=200, blank=True, null=True)
    merknader = models.CharField(max_length=2000, blank=True, null=True)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'leverandor'


class Ordre(models.Model):
    ordre_id = models.AutoField(primary_key=True)
    ordre_dato = models.DateTimeField()
    kunde = models.ForeignKey(Kunde, models.DO_NOTHING)
    status = models.ForeignKey('Ordrestatus', models.DO_NOTHING, db_column='status')
    belop_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    mva_belop = models.DecimalField(max_digits=7, decimal_places=2)
    totalbelop = models.DecimalField(max_digits=7, decimal_places=2)
    notat = models.CharField(max_length=2000, blank=True, null=True)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'ordre'


class Ordrelinje(models.Model):
    ordrelinje_id = models.AutoField(primary_key=True)
    ordre = models.ForeignKey(Ordre, models.DO_NOTHING)
    linjenr = models.PositiveIntegerField()
    antall = models.PositiveIntegerField()
    rabatt_pros = models.PositiveIntegerField()
    belop_linje_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    kommentar = models.CharField(max_length=200, blank=True, null=True)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)
    produkt = models.ForeignKey('Vare', models.DO_NOTHING)

    class Meta:
        db_table = 'ordrelinje'
        unique_together = (('ordre', 'linjenr'),)

class Ordrestatus(models.Model):
    statuskode = models.CharField(primary_key=True, max_length=10)
    beskrivelse = models.CharField(max_length=200)

    class Meta:
        db_table = 'ordrestatus'


class Vare(models.Model):
    produkt_id = models.AutoField(primary_key=True)
    produktkode = models.CharField(unique=True, max_length=12, blank=True, null=True)
    produktnavn = models.CharField(max_length=80)
    beskrivelse = models.CharField(max_length=4000, blank=True, null=True)
    produktkategori = models.CharField(max_length=128, blank=True, null=True)
    produkttype = models.CharField(max_length=128, blank=True, null=True)
    produktopprinnelse = models.CharField(max_length=128, blank=True, null=True)
    produktaar = models.CharField(max_length=128, blank=True, null=True)
    leverandor = models.ForeignKey(Leverandor, models.DO_NOTHING, blank=True, null=True)
    pris_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    beholdning = models.PositiveIntegerField()
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'vare'

class Varepris(models.Model):
    varepris_id = models.AutoField(primary_key=True)
    produkt = models.ForeignKey(Vare, models.DO_NOTHING)
    pris_fra_dato = models.DateField()
    pris_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    reg_dato = models.DateTimeField(blank=True, null=True)
    reg_bruker = models.CharField(max_length=20, blank=True, null=True)
    endret_dato = models.DateTimeField(blank=True, null=True)
    endret_bruker = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'varepris'
        unique_together = (('produkt', 'pris_fra_dato'),)

# Views

class v_ordrelinje(models.Model):
    ordrelinje_id = models.AutoField(primary_key=True)
    ordre = models.ForeignKey(Ordre, models.DO_NOTHING)
    produkt = models.ForeignKey(Vare, models.DO_NOTHING)
    linjenr = models.PositiveIntegerField()
    antall = models.PositiveIntegerField()
    rabatt_pros = models.PositiveIntegerField()
    belop_linje_u_mva = models.DecimalField(max_digits=7, decimal_places=2)
    kommentar = models.CharField(max_length=200, blank=True, null=True)
    produktkode = models.CharField(max_length=12, blank=True, null=True)
    produktnavn = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'v_ordrelinje'
