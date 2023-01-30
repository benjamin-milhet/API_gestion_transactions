# GHYS_MILHET_4A_ILC_WORKFLOW

## Membres du groupe
 - Clément GHYS
 - Benjamin MILHET
 
 ### ILC

### Documentation de la classe Personne.py

#### Attributs

- prenom : str
- solde : float
- transactions : list

#### Méthodes

- __init__(self, prenom, solde)
Démarrage de la classe Personne, initialisation des attributs

- __str__(self)
Affichage de la classe Personne, permet d'afficher les attributs de la classe
en format str. La liste des transactions associées à la personne est triée par ordre croissant.

- sortTransactionsParDate(self)
Tri de la liste des transactions par ordre croissant de date.