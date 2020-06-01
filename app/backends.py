from django.contrib.auth.models import update_last_login
from django.contrib.auth.signals import user_logged_in
from .models import Uzytkownik
from django.conf import settings



class UserAuthBackend(object):
    def authenticate(self, request, email=None,haslo=None):
        try:
            user = Uzytkownik.objects.get(email=email)

            if haslo == getattr(user,'haslo'):
                return user
            else:
                return None
        except Uzytkownik.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return Uzytkownik.objects.get(pk=user_id)
        except Uzytkownik.DoesNotExist:
            return None

user_logged_in.disconnect(update_last_login, dispatch_uid='update_last_login')