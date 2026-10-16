from tournoi.models import Equipe,Match
import pytest


@pytest.fixture
def equipe_lion(db):
    equipe = Equipe.objects.create(nom="Lion ravage",promo="L1")
    return equipe

@pytest.fixture
def equipe_shark(db):
    equipe = Equipe.objects.create(nom="sharknadose",promo="L2")
    return equipe




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



def test_un_match_oppose_equipe_visitese_equipe_recoit_a_une_date_donnee(db,equipe_lion,equipe_shark):
    mach = Match.objects.create(domicile=equipe_lion,visiteuse=equipe_shark,date="2024-06-10")
    assert mach.domicile
    assert mach.visiteuse
    assert mach.date




def test_tant_qu_un_match_non_joue_score_est_inconnu(db,equipe_lion,equipe_shark):
    match = Match.objects.create(domicile=equipe_lion,visiteuse=equipe_shark)
    assert match.score == None












     
    
