from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, phone, first_name, last_name, password, **extra_fields):
        user = self.model(phone=phone, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, password, phone):
        return self._create_user(phone, first_name, last_name, password)

    def create_superuser(self, first_name, last_name, password, phone):
        extra_fields = {
            "is_staff": True,
            "is_superuser": True
        }
        return self._create_user(phone, first_name, last_name, password, **extra_fields)
