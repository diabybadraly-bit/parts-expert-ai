# PARTS EXPERT AI - Documentation & Instructions de Démarrage

## Description du Projet
PARTS EXPERT AI est une application web intelligente de gestion, recherche et catalogue de pièces détachées automobiles, développée sous Python avec Flask et SQLite.

## Structure du Projet
- `C:/Users/HP/PARTS_EXPERT_AI/app.py` : Application principale Flask (API et Interface Web)
- `C:/Users/HP/PARTS_EXPERT_AI/parts_expert.db` : Base de données SQLite initiale
- `C:/Users/HP/PARTS_EXPERT_AI/test_app.py` : Tests unitaires (Pytest)
- `C:/Users/HP/PARTS_EXPERT_AI/requirements.txt` : Dépendances du projet

## Instructions de Démarrage

1. Prérequis : Python 3.x installé sur Windows.
2. Installation des dépendances :
   ```bash
   pip install -r C:/Users/HP/PARTS_EXPERT_AI/requirements.txt
   ```
3. Lancement de l'application :
   ```bash
   python C:/Users/HP/PARTS_EXPERT_AI/app.py
   ```
4. Accès à l'interface web :
   Ouvrir un navigateur et pointer sur : `http://localhost:5000`

## Lancement des Tests
```bash
python -m pytest C:/Users/HP/PARTS_EXPERT_AI/test_app.py
```
