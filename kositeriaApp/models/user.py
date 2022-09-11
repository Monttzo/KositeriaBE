from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class user(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    nameUser = models.CharField('nameUser', max_length = 50)
    lastNameUser = models.CharField('lastNameUser', max_length = 50)
    username = models.CharField('username', max_length = 25, unique=True)
    password = models.CharField('passwordUser', max_length = 256)
    emailUser = models.EmailField('emailUser', max_length = 100, null=True)
    dateBirthUser = models.DateField('dateBirthUser')
    appMode = models.BooleanField('appMode', default = False)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'