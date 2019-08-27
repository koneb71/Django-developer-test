import uuid

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UsersManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Step(models.Model):
    name = models.CharField(max_length=255)
    explanation = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RoadMap(models.Model):
    name = models.CharField(max_length=255)
    steps = models.ManyToManyField(Step)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    roadmap = models.ForeignKey(RoadMap, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name