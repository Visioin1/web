from django.db import models
from base.models import Base_Model



class Home(Base_Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    home_image=models.ImageField(upload_to="home")



class Internships(Base_Model):
    internship_name=models.CharField(max_length=100)
    internship_description=models.TextField()
    internship_logo=models.ImageField(upload_to="internship")
    


class jobs(Base_Model):
    company_name=models.CharField(max_length=100)
    company_location=models.CharField(max_length=100)
    position=models.CharField(max_length=100,default="")
    apply_link=models.CharField(max_length=300)