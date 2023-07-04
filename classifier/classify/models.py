from django.db import models

# Create your models here.
class Test_Image(models.Model):
    name=models.CharField(max_length=150,null=True,blank=True)
    image=models.ImageField(upload_to='images/',null=False,blank=False)

    def __str__(self):
        return self.name