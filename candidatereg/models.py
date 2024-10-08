from django.db import models
from PIL import Image
from django import forms

from voter.models import VoterList
dpt= [
    ("Information Technology", "Information Technology"),]
gender=[('m','male'),('f','female')]
# Create your models here.

class Candidates(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    second_name=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=50,choices=gender,null=True)
    department=models.CharField(max_length=50,choices=dpt,null=True)
    rno = models.CharField(max_length=10,null=False)
    email=models.EmailField(max_length=50,null=True)
    photo=models.ImageField(default='default.jpg',upload_to='candidate_pics/')
    votes=models.IntegerField(default=0,blank=True)
    def __str__(self):
        return str(self.rno)
    
    # def save(self,*args,**kwargs):
    #     super(). save(*args,**kwargs)
    #     img= Image.open(self.photo.path)
    #     if img.height>150 or img.width>150:
    #         output_size=(150,150)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)
    
    
