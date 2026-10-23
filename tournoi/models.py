from django.db import models  # noqa: F401

class Equipe(models.Model):
    nom = models.CharField(max_length=255 , unique=True)
    promo = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nom 

class Match(models.Model):
    domicile = models.ForeignKey(
        Equipe,
        related_name='equipe_domiciles',
        on_delete=models.CASCADE,
    )
    
    visiteuse = models.ForeignKey(
        Equipe,
        related_name='matchs_visiteuse',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    
    score = models.CharField(null=True)
    
    def __str__(self):
        return f"{self.domicile.nom} : {self.score}"
    
    
    