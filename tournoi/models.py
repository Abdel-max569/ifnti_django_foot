from django.db import models  # noqa: F401

class Equipe(models.Model):
    nom = models.CharField(max_length=255 , unique=True)
    promo = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nom +' '+self.promo

