"""
Definition of models.
"""
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import update_last_login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
user_logged_in.disconnect(update_last_login, dispatch_uid='update_last_login')


class OpiekunSali(models.Model):
    id_opiekuna = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank=True, null=True)
    numer_telefonu = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opiekun_sali'
        verbose_name_plural = 'Opiekunowie Sali'
    def __str__(self):
        dane=self.imie + " " + self.nazwisko
        return dane
        


class Rezerwacja(models.Model):
    id_rezerwacji = models.AutoField(primary_key=True)
    id_uzytkownika = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='id_uzytkownika')
    czy_anulowana = models.BooleanField()


    class Meta:
        managed = True
        db_table = 'rezerwacja'
        verbose_name = 'Rezerwacja'
        verbose_name_plural = 'Rezerwacje'


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
        verbose_name_plural = 'Rezerwacje Stanowiska'
    def anuluj(self):
        if self.czy_anulowana==False:
            return "Nie"
        else:
            return "Tak"

class RodzajSali(models.Model):
    id_rodzaju_sali = models.AutoField(primary_key=True)
    rodzaj = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rodzaj_sali'
        verbose_name_plural = 'Rodzaje Sali'
    def __str__(self):
        return self.rodzaj

class Rola(models.Model):
    id_roli = models.AutoField(primary_key=True)
    nazwa_roli = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rola'
        verbose_name_plural = 'Role'
    def __str__(self):
        return str(self.id_roli) 

class Sala(models.Model):
    id_sali = models.AutoField(primary_key=True)
    nazwa_sali = models.CharField(max_length=128)
    budynek = models.CharField(max_length=64, blank=True, null=True)
    opis_sali = models.TextField(blank=True, null=True)
    id_rodzaju_sali = models.ForeignKey(RodzajSali, models.DO_NOTHING, db_column='id_rodzaju_sali')


    class Meta:
        managed = False
        db_table = 'sala'
        verbose_name_plural = 'Sale'
    def __str__(self):
        return self.nazwa_sali

class Stanowisko(models.Model):
    id_stanowiska = models.AutoField(primary_key=True)
    id_sali = models.ForeignKey(Sala, models.DO_NOTHING, db_column='id_sali')
    nazwa_stanowiska = models.CharField(max_length=128)
    opis_stanowiska = models.TextField(blank=True, null=True)
    stopien_zaawansowania = models.IntegerField(("Stopień zaawansowania (1-10)"),
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)] )
    czy_dostepne = models.BooleanField()
    id_sali = models.ForeignKey(Sala, models.CASCADE, db_column='id_sali')

    class Meta:
        managed = True
        db_table = 'stanowisko'
        verbose_name_plural = 'Stanowiska'
    def status(self):
        if self.czy_dostepne==False:
            return "Nie"
        else:
            return "Tak"
    def __str__(self):
        dane = self.nazwa_stanowiska + " id: " + str(self.id_stanowiska)
        return dane

class SalaOpiekun(models.Model):
    id_sala_opiekun = models.AutoField(primary_key=True)
    id_sali = models.ForeignKey(Sala, models.DO_NOTHING, db_column='id_sali')
    id_opiekuna_sali = models.ForeignKey(OpiekunSali, models.DO_NOTHING, db_column='id_opiekuna_sali')

    class Meta:
        managed = False
        db_table = 'sala_opiekun'
        verbose_name_plural = 'SalaOpiekun'

class Uzytkownik(models.Model):
    id_uzytkownika = models.AutoField(primary_key=True)
    id_roli = models.ForeignKey(Rola, models.DO_NOTHING, db_column='id_roli')
    imie = models.CharField(max_length=64, blank=True, null=True)
    nazwisko = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=128)
    haslo = models.CharField(max_length=128)

    is_superuser = models.IntegerField(default=False)
    is_staff = models.BooleanField(('staff status'),default=False)

    def __str__(self):
        dane=self.imie + " " + self.nazwisko
        return dane


    def is_active(self):
     return True

    def get_username(self):
     return self.email

    def is_authenticated(self):
        return False

    def has_perm(self, perm, obj=None):
     return self.is_superuser

    def has_module_perms(self, app_label):
     return self.is_superuser
    
    class Meta:
        managed = True
        db_table = 'uzytkownik'
        verbose_name_plural = 'Użytkownicy'
