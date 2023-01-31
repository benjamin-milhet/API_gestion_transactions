# API de gestion de transactions

## Membres du groupe
 - Clément GHYS
 - Benjamin MILHET
 
### ILC

### Documentation du chargement des fichiers de données

#### Fonction chargerFichier

Cette fonction permet de charger les données de deux fichiers CSV, l'un permettant de charger des personnes et l'autre permettant de charger des transactions entre ces différentes personnes.
On commence d'abord par charger les personnes parce que nous avons besoins de ces données pour pouvoir charger les transactions.
Nous avons décidé de charger les deux fichiers en même temps afin que les transactions ne soit pas charger afin des personnes, ce qui pourrait poser problème plus tard lors d'appelle d'autre fonction.

##### Paramètre de la requête curl

- fichierPersonne : str
- fichierTransaction : str
- delimiter : str

Cette fonction appelle successivement 2 fonctions, la première pour charger les personnes avec comme paramètre le nom du fichier de données contenant les personnes.
Puis appelle une deuxième fonction permettant de charger les transactions. Elle retourne le nombre de lignes chargées pour chacun des deux fichiers.

#### Nom des fichiers

 - Fichier contenant les personnes : data.csv
 - Fichier contenant les transactions : transactions.csv



