from django.shortcuts import render
from .models import Home,Internships,jobs
# Create your views here.
def home(request):
   
        
        
    context={"home_data":Home.objects.all(),"Internships":Internships.objects.all(),"jobs":jobs.objects.all()}
    return render(request,"home/home.html",context)