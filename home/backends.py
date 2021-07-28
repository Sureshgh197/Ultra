from django.contrib.auth.backends import BaseBackend
from home.models import AppUsers

class MyBackend(BaseBackend):
    def authenticate(email=None, password=None):
        try:
            appUser = AppUsers.objects.get(email=email)
            if appUser.check_password(password) is True:
                print('user authenticated')
                return appUser
        except AppUsers.DoesNotExist:
            return None
