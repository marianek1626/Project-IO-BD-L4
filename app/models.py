"""
Definition of models.
"""
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import update_last_login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

#class users(models.Model):
#    active=models.IntegerField()
#    email=models.CharField(max_length=30)
#    password=models.CharField(max_length=30)
#    name=models.CharField(max_length=10)
#    lastname=models.CharField(max_length=10)
    

#    def _str_(self):
#        return self.firstname

#def update_last_login(sender, user, **kwargs):
#    """
#    A signal receiver which updates the last_login date for
#    the user logging in.
#    """
#    user.last_login = timezone.now()
#    user.save(update_fields=['last_login'])
user_logged_in.disconnect(update_last_login, dispatch_uid='update_last_login')


class OpiekunSali(models.Model):
    id_opiekuna = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank=True, null=True)
    numer_telefonu = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'opiekun_sali'
        verbose_name_plural = 'Opiekunowie Sali'


class Rezerwacja(models.Model):
    id_rezerwacji = models.AutoField(primary_key=True)
    id_uzytkownika = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='id_uzytkownika')
    event_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    czy_anulowana = models.BooleanField()
    event_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.event_name)

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


class RodzajSali(models.Model):
    id_rodzaju_sali = models.AutoField(primary_key=True)
    rodzaj = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rodzaj_sali'
        verbose_name_plural = 'Rodzaje Sali'

class Rola(models.Model):
    id_roli = models.AutoField(primary_key=True)
    nazwa_roli = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'rola'
        verbose_name_plural = 'Role'

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
        verbose_name_plural = 'Sale'

class Stanowisko(models.Model):
    id_stanowiska = models.AutoField(primary_key=True)
    id_sali = models.ForeignKey(Sala, models.DO_NOTHING, db_column='id_sali')
    nazwa_stanowiska = models.CharField(max_length=128)
    opis_stanowiska = models.TextField(blank=True, null=True)
    stopien_zaawansowania = models.IntegerField()
    czy_dostepne = models.BooleanField()
    #zdjecie = models.ImageField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stanowisko'
        verbose_name_plural = 'Stanowiska'



class Uzytkownik(models.Model):
    id_uzytkownika = models.AutoField(primary_key=True)
    id_roli = models.ForeignKey(Rola, models.DO_NOTHING, db_column='id_roli')
    imie = models.CharField(max_length=64, blank=True, null=True)
    nazwisko = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=128)
    haslo = models.CharField(max_length=128)

    is_superuser = models.IntegerField(default=False)
    #last_login = models.DateTimeField(('last login'), default=timezone.now)
    is_staff = models.BooleanField(('staff status'),default=False)

    def is_active(self):
     return True

    def get_username(self):
     return self.email

    def is_authenticated(self):
        return True

    def has_perm(self, perm, obj=None):
     return self.is_superuser

    def has_module_perms(self, app_label):
     return self.is_superuser
    
    class Meta:
        managed = True
        db_table = 'uzytkownik'
        verbose_name_plural = 'Użytkownicy'
