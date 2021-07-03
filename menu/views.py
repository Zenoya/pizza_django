from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.*


# creation des vues
# view index qui se charge si rien après menu/
def index(request):
    '''
    # On récupère les pizzas dans la bdd
    pizzas = Pizza.objects.all()
    # On met dans une collection les noms des pizzas et les prix
    pizzas_names_price = [pizza.nom + " : " + str(pizza.prix) + "€"for pizza in pizzas]
    # On créé une chaine avec les nom séparés par une ,
    pizzas_names_price_str = ", ".join(pizzas_names_price)
    # On affiche
    return HttpResponse(f"Les pizzas : {pizzas_names_price_str}")
    '''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all()
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)
