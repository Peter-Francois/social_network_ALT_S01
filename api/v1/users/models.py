from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Gestionnaire personnalisé
class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, birthdate, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, birthdate, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, firstname, lastname, birthdate, password, **extra_fields)

# Utilisateur personnalisé
class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    birthdate = models.DateField()
    avatar = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Champs requis pour l'authentification
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "birthdate"]

    # Utilisation du gestionnaire personnalisé
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.email})"
