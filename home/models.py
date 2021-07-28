from django.db import models
#from home.backends import MyBackend
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import sys
# Create your models here.


# class Slider(models.Model):

#     img=models.ImageField()
#     name=models.CharField(max_length=200)


class UImages(models.Model):
    
    imag=models.ImageField(upload_to='pics/')
    

    def save(self):
        im = Image.open(self.imag)
        output = BytesIO()
        im = im.resize( (1060,360) )
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.imag = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imag.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(UImages,self).save()

class UserManager(BaseUserManager):
      def create_user(self, email, profile_picture,first_name,last_name,phone,username,DOB,password):
          if not email:
             raise ValueError('user must have email address')
         
          user = self.model(
            email=self.normalize_email(email),
            profile_picture=profile_picture,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            username=username,
            DOB=DOB,
                   )

          user.set_password(password)
          user.save(using=self._db)

          return user

      def create_superuser(self, email,password,**extra_fields):
                user = self.model(email=self.normalize_email(email),)
                user.staff=True
                user.admin=True
                user.set_password(password)
                user.save(using=self._db)
                return user

      


      


class AppUsers(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=True,
        editable=True,
    
    )
    profile_picture        =models.ImageField(upload_to='profile_pichurs/',null=True)
    first_name             =models.CharField(max_length=255,null=True)
    last_name              =models.CharField(max_length=255,null=True)
    phone                  =models.BigIntegerField(null=True)
    username               =models.CharField(max_length=255,null=True)
    DOB                    =models.DateField(null=True)
    password               =models.CharField(max_length=255)
    staff                  =models.BooleanField(default=False) # a admin user; non super-user
    admin                  =models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.
    #backend=MyBackend
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects=UserManager()

    def get_uname(self):
        # The user is identified by their email address
        return self.username

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.first_name

    # def __str__(self):
    #     return self.email+' '+self.first_name+' '+self.last_name

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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
       
  

    #   def create_superuser(self, email, password=None, **extra_fields):
    #             user=self._create_user(email, password, True, True, **extra_fields)
    #             user.save(using=self._db)
    #             return user

    


