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


class pdfImage(models.Model):
    
    imag=models.ImageField(upload_to='pdfs/')
    

    # def save(self):
    #     im = Image.open(self.imag)
    #     output = BytesIO()
    #     im = im.resize( (1060,360) )
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)
    #     self.imag = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imag.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
    #     super(UImages,self).save()
