from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401
from tournoi.models import Equipe, Match

def pages_test_affichage(request):
    return render(
        request,
        "tournoi/list_match.html",
        {
            "matchs" : Match.objects.select_related("domicile","visiteuse").all()
        }
                                   
    )
    
    
    
    