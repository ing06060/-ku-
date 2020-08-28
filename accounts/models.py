from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
"""
class Profile(models.Model):
    GRADES = (
        ('freshman', '1학년'),
        ('sophomore', '2학년'),
        ('junior', '3학년'),
        ('senior', '4학년'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10, verbose_name='닉네임')
    major = models.TextField(max_length=20, null=True, verbose_name='학과')
    #major_one = models.TextField(max_length=20, null=True)
    #major_two = models.TextField(max_length=20, null=True)
    grade = models.PositiveSmallIntegerField(null=True, choices=GRADES, verbose_name='학년')
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD = User.username
"""


class Profile(AbstractUser):
    GRADES = (
        ('1학년', '1학년'),
        ('2학년', '2학년'),
        ('3학년', '3학년'),
        ('4학년', '4학년'),
    )
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(max_length=30)
    nickname = models.TextField(max_length=10)
    major = models.TextField(max_length=20, null=True)
    grade = models.CharField(max_length=20, null=True, choices=GRADES)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return "<%d %s>" % (self.pk, self.email)

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password,**extra_fields):
        if not email:
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, password, **extra_fields)

"""
class Profile(models.Model):
    GRADES = (
        ('freshman', '1학년'),
        ('sophomore', '2학년'),
        ('junior', '3학년'),
        ('senior', '4학년'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    major = models.TextField(max_length=20, null=True)
    #major_one = models.TextField(max_length=20, null=True)
    #major_two = models.TextField(max_length=20, null=True)
    grade = models.PositiveSmallIntegerField(null=True, choices=GRADES)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()   
"""