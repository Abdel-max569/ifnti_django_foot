from tournoi.models import Equipe
import pytest
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Lion ravage",promo="L1")
    assert equipe.nom
    assert equipe.promo

def test_deux_equipe_ne_pas_avoir_meme_nom(db):
    equipe1 = Equipe.objects.create(nom="Lion ravage",promo="L1")
    with pytest.raises(Exception):
        equipe2 = Equipe.objects.create(nom="Lion ravage",promo="L2")

