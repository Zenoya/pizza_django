from django.urls import path
from . import views

app_name = 'main'

# Les différents patterns d'url
urlpatterns = [
    # Si rien => on charge index dans views
    path('', views.index, name="index"),
]