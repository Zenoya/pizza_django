from django.urls import path
from . import views


app_name = 'menu'

# Les différents patterns d'url
urlpatterns = [
    # Si rien => on charge index dans views
    path('GetPizzas', views.api_get_pizzas,),
]