from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.dispatch import receiver
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.apps import apps
import uuid

# CustomUserManager extended from BaseUserManager
# removed the username field from create_user function since 
# no email should be required to create user and superuser
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class Country(models.Model):
  name = models.CharField(max_length = 50)
  alpha_two_code = models.CharField(max_length = 2)

# custom User model with addditional fields of country, gender, phone and UserType
# changed the username field to email since we will use email for authentication 
# and registration
class UserType(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class User(AbstractUser):
  GenderChoices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Don\'t Specify'),
  ]
  email = models.EmailField(verbose_name='email', unique=True, max_length=255)
  phone = models.CharField(null=True, max_length=50)
  country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
  user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, default=4)
  gender = models.CharField(
        max_length=1,
        choices=GenderChoices,
        null=True
    )
  REQUIRED_FIELDS = []
  USERNAME_FIELD = 'email'

  objects = CustomUserManager()

  def get_username(self):
    return self.email
    
# generate a random username and check if its already taken. 
# If taken, generate a username again until we find a valid username
def generate_username(instance):
  val = uuid.uuid4().hex[:30]
  x=0
  while True:
      if x == 0 and User.objects.filter(username=val).count() == 0:
        return val
      else:
        new_val = uuid.uuid4().hex[:30]
        if User.objects.filter(username=new_val).count() == 0:
          return new_val
      x += 1
      if x > 1000000:
        raise Exception("Name is super popular!")

def pre_save_post_receiver(sender, instance, *args,**kwargs):
  if not instance.username:
    instance.username= generate_username(instance)

#save the username before the User model is saved with the unique username
models.signals.pre_save.connect(pre_save_post_receiver, sender=User)