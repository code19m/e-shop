from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password=None, **extra_fields):
        """Create and save a User with the given email and password."""

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        extra_fields.setdefault("first_name", "Nuriddin")
        extra_fields.setdefault("last_name", "Obidjonov")
        extra_fields.setdefault("second_name", "Olimjon o'g'li")
        extra_fields.setdefault("role", "stockman")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
