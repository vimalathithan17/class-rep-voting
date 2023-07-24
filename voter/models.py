from django.db import models
from PIL import Image
# Create your models here.

class VoterList(models.Model):
    rno = models.CharField(max_length = 10, null=False, unique=True, primary_key=True)
    name = models.CharField(max_length = 50, null=True, blank=True)
    dpt= [
    ("Information Technology", "Information Technology"),]
    dept= models.CharField(max_length = 50,choices=dpt, null=True, blank=True)
    voter_image= models. ImageField(default='default.jpg',upload_to='voter_pics/')
    voted=models.BooleanField(default=False)
    def __str__(self):
        return f'voter {self.rno}'
        
    def save(self,*args,**kwargs):
        super(). save(*args,**kwargs)
        img= Image.open(self.voter_image.path)
        if img.height>150 or img.width>150:
            output_size=(150,150)
            img.thumbnail(output_size)
            img.save(self.voter_image.path)
            


