# Tournoi de foot inter-promos

Dépôt de départ du TD **TDD ping-pong** — cours Django, L3, IFNTI Sokodé.

Un projet Django 5.2 vide, prêt à tester : une application `tournoi` sans modèle, un gabarit
`base.html`, `pytest-django` configuré et un test qui passe.

## Installer

```bash
uv sync
uv run pytest
uv run python manage.py runserver
```

## Règles du jeu

À chaque round, on change de rôle sur ce dépôt :

- **qui écrit les tests** ne modifie que le dossier `tests/` ;
- **qui implémente** modifie tout, **sauf** `tests/`, et ne lit que les tests : ils sont la
  seule spécification.

Tout ce qui passe les tests est permis. Un test qui laisse passer du code faux est un test à
renforcer, pas une tricherie.

Avant de commencer : `git pull`. Pour finir : `git push`.
