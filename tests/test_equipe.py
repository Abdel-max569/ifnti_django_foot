from tournoi.models import Equipe

def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Lion ravage",promo="L1")
    assert equipe.nom
    assert equipe.promo
    
