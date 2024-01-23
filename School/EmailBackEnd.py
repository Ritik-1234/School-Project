from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
[]


class EmailBackEnd(ModelBackend):
    def authenticate(self,  username=None, password= None, **kwargs):
        Usermodel = get_user_model()
        try:
            user = Usermodel.objects.get(email=username)
        except Usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
