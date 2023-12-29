"""
Django models for user account management.
    Classes: - Account: Custom user model representing an account.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifiers
       for authentication instead of usernames."""
    def create_user(self, first_name, last_name, username, email, password=None):
        """Create and save a user with the given email and password."""

        if not email:
            raise ValueError("Email must be set.")

        if not username:
            raise ValueError("Username must be set.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """Custom user model representing an account."""
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    # required
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email) if self.email else "No email"

    def has_perm(self, permission, obj=None):
        """
        Check if the user has a specific permission.
        Returns bool: True if the user has the specified permission, False otherwise.
        """
        return self.is_admin

    def has_module_perms(self, add_label):
        """Check if the user has any permissions to view the app `app_label`."""
        return True
