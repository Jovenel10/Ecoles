from django.contrib import admin
from .models import Etudiants

class affichageTable(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'pays', 'adresse', 'telephone')  # Assurez-vous que les noms des champs correspondent aux attributs de votre modèle Etudiants

admin.site.register(Etudiants, affichageTable)
