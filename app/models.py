"""
Definition of models.
"""

from django.db import models

# Create your models here.

#class users(models.Model):
#    active=models.IntegerField()
#    email=models.CharField(max_length=30)
#    password=models.CharField(max_length=30)
#    name=models.CharField(max_length=10)
#    lastname=models.CharField(max_length=10)
    

#    def _str_(self):
#        return self.firstname




class OpiekunSali(models.Model):
    id_opiekuna = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank=True, null=True)
    numer_telefonu = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'opiekun_sali'


class Rezerwacja(models.Model):
    id_rezerwacji = models.AutoField(primary_key=True)
    id_uzytkownika = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='id_uzytkownika')
    data_zgloszenia = models.DateTimeField()
    czy_anulowana = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'rezerwacja'


class RezerwacjaStanowiska(models.Model):
    id_rezerwacji_stanowiska = models.AutoField(primary_key=True)
    id_rezerwacji = models.ForeignKey(Rezerwacja, models.DO_NOTHING, db_column='id_rezerwacji')
    id_stanowiska = models.ForeignKey('Stanowisko', models.DO_NOTHING, db_column='id_stanowiska')
    termin_rozpoczecia = models.DateTimeField()
    termin_zakonczenia = models.DateTimeField()
    czy_anulowana = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'rezerwacja_stanowiska'


class RodzajSali(models.Model):
    id_rodzaju_sali = models.AutoField(primary_key=True)
    rodzaj = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rodzaj_sali'


class Rola(models.Model):
    id_roli = models.AutoField(primary_key=True)
    nazwa_roli = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rola'


class Sala(models.Model):
    id_sali = models.AutoField(primary_key=True)
    id_rodzaju_sali = models.ForeignKey(RodzajSali, models.DO_NOTHING, db_column='id_rodzaju_sali')
    id_opiekuna = models.ForeignKey(OpiekunSali, models.DO_NOTHING, db_column='id_opiekuna', blank=True, null=True)
    nazwa_sali = models.CharField(max_length=128)
    budynek = models.CharField(max_length=64, blank=True, null=True)
    opis_sali = models.TextField(blank=True, null=True)
    zdjecie = models.ImageField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sala'


class Stanowisko(models.Model):
    id_stanowiska = models.AutoField(primary_key=True)
    id_sali = models.ForeignKey(Sala, models.DO_NOTHING, db_column='id_sali')
    nazwa_stanowiska = models.CharField(max_length=128)
    opis_stanowiska = models.TextField(blank=True, null=True)
    stopien_zaawansowania = models.IntegerField()
    czy_dostepne = models.BooleanField()
    zdjecie = models.ImageField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stanowisko'


class Uzytkownik(models.Model):
    id_uzytkownika = models.AutoField(primary_key=True)
    id_roli = models.ForeignKey(Rola, models.DO_NOTHING, db_column='id_roli')
    imie = models.CharField(max_length=64, blank=True, null=True)
    nazwisko = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=128)
    haslo = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'uzytkownik'