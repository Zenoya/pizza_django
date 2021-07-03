from django.contrib import admin
from .models import Pizza


# class PizzaAdmin pour afficher les infos qu'on souhaite sur interface admin
class PizzaAdmin(admin.ModelAdmin):
    # ajout des infos qu'on veut voir
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    # ajout de champs  de recherche
    search_fields = ['nom']


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
