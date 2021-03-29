from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None):
        '''Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('Users must have an Email address!')
        user = self.model(
            email=self.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    GENDER_OPTIONS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    CLASSSTANDING_OPTIONS = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ]

    email           = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    username        = models.CharField(verbose_name='Email', max_length=60, null=True, blank=True)
    fname           = models.CharField(verbose_name='First Name', max_length=60)
    lname           = models.CharField(verbose_name='Last Name', max_length=60)
    dob             = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    phone           = models.CharField(max_length=10, null=False, verbose_name="Contact Number")
    gender          = models.CharField(verbose_name='Gender', max_length=6, choices=GENDER_OPTIONS)
    classstandings  = models.CharField(verbose_name='Class Standing', max_length=10, choices=CLASSSTANDING_OPTIONS)
    major           = models.CharField(verbose_name='Major', max_length=100, null=True)
    date_joined     = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.fname + " " + self.lname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
