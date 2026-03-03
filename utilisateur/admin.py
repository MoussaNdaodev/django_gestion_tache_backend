from django.contrib import admin

from utilisateur.models import Utilisateur

# Register your models here.
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'role', 'date_creation')
    search_fields = ('email', 'nom', 'prenom')