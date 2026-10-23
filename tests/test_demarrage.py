def test_le_projet_demarre(client):
    reponse = client.get("/admin/login/")
    assert reponse.status_code == 200


