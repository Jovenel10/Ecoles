from django.contrib import admin
from .models import Etudiants

# Register your models here.
class affichageTable(admin.ModelAdmin):
    liste_display = ['Id', 'Prenom', 'Nom', 'Pays','Adresse',' Telephone']
admin.site.register(Etudiants,affichageTable)