from django.urls import path  # noqa: F401

from . import views  # noqa: F401

app_name = "tournoi"

urlpatterns = [
    path("matches",views.pages_test_affichage)
]
