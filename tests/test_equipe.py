from tournoi.models import Equipe, Match
import pytest


@pytest.fixture
def equipe_lion():
    equipe = Equipe.objects.create(nom="Lion ravage", promo="L1")
    return equipe


@pytest.fixture
def equipe_shark():
    equipe = Equipe.objects.create(nom="sharknadose", promo="L2")
    return equipe


@pytest.fixture
def equipe_invencible_l3():
    equipe = Equipe.objects.create(nom="Invencible l3", promo="L3")
    return equipe


@pytest.fixture
def match1(equipe_lion, equipe_shark):
    match = Match.objects.create(
        domicile=equipe_lion, visiteuse=equipe_shark, date="2024-06-20", score="4-0"
    )
    return match


@pytest.fixture
def match2(equipe_invencible_l3, equipe_shark):
    match = Match.objects.create(
        domicile=equipe_invencible_l3,
        visiteuse=equipe_shark,
        date="2024-06-10",
        score="70-0",
    )
    return match


def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe = Equipe.objects.create(nom="Lion ravage", promo="L1")
    assert equipe.nom
    assert equipe.promo


def test_deux_equipe_ne_pas_avoir_meme_nom(db):
    equipe1 = Equipe.objects.create(nom="Lion ravage", promo="L1")
    with pytest.raises(Exception):
        equipe2 = Equipe.objects.create(nom="Lion ravage", promo="L2")


def test_une_equipe_s_affiche_avec_son_nom(db):
    nom_equipe = "Lion ravage"
    equipe = Equipe.objects.create(nom=nom_equipe, promo="L1")
    assert nom_equipe == str(equipe)


def test_un_match_oppose_equipe_visitese_equipe_recoit_a_une_date_donnee(
    db, equipe_lion, equipe_shark
):
    mach = Match.objects.create(
        domicile=equipe_lion, visiteuse=equipe_shark, date="2024-06-10"
    )
    assert mach.domicile
    assert mach.visiteuse
    assert mach.date


def test_tant_qu_un_match_non_joue_score_est_inconnu(db, equipe_lion, equipe_shark):
    match = Match.objects.create(
        domicile=equipe_lion, visiteuse=equipe_shark, date="2024-06-12"
    )
    assert match.score == None


def test_un_match_s_affiche_avec_le_score_et_equipe_domicile(
    db, equipe_lion, equipe_shark
):
    match = Match.objects.create(
        domicile=equipe_lion, visiteuse=equipe_shark, date="2024-06-10", score="4-0"
    )
    assert str(match) == f"{match.domicile.nom} : {match.score}"


def test_list_tous_matches_s_affiche(client, db, match1, match2):
    response = client.get("/matches")
    assert match1.date in response.text
    assert match2.date in response.text

def test_page_affichage_une_equipe(client,db,equipe_shark):
    response = client.get(f"/equipes/{equipe_shark.id}")
    assert response.status_code == 200
    assert equipe_shark.nom in response.text
    assert equipe_shark.promo in response.text



