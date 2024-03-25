
from django.shortcuts import render
from django.http import HttpResponse
from ecole.models import Etudiants

# Create your views here.
def affichage(request):
   ecole=Etudiants.objects.all()
   #return HttpResponse(ecole)

   return render(request,'index.html', {'Etudiants': ecole})
