from django.db import models


# définir le model de pizza pour la BDD
class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    # Afficher le nom des pizzas dans l'interface admin django
    def __str__(self):
        return self.nom

