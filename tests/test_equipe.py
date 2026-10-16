from tournoi.models import Equipe
from tournoi.models import Macth

import pytest
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Lion ravage",promo="L1")
    assert equipe.nom
    assert equipe.promo

def test_deux_equipe_ne_pas_avoir_meme_nom(db):
    equipe1 = Equipe.objects.create(nom="Lion ravage",promo="L1")
    with pytest.raises(Exception):
        equipe2 = Equipe.objects.create(nom="Lion ravage",promo="L2")


def test_une_equipe_s_affiche_avec_son_nom(db):
    nom_equipe = "Lion ravage"
    equipe = Equipe.objects.create(nom=nom_equipe,promo="L1")
    assert nom_equipe == str(equipe)



def test_un_match_oppose_equipe_visitese_equipe_recoit_a_une_date_donnee(db):
    equipe_recoit = Equipe.objects.create(nom="Lion ravage",promo="L1")
    equipe_visitese = Equipe.objects.create(nom="Lion ravage",promo="L1")
    mach = Macth.objects.create(domicile=equipe_recoit,visiteuse=equipe_visitese,date="2024-06-10")
    assert mach.domicile
    assert mach.visiteuse
    assert mach.date















     
    
