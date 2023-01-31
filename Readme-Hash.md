# API de gestion de transactions

## Membres du groupe
 - Clément GHYS
 - Benjamin MILHET
 
## ILC

## Documentation du Hachage

Nous utilisons une fonctions de hachage afin de sécuriser nos transactions. Pour cela nous utilisons le nom des deux personnes et la somme du transfert d'argent.

### Choix de la fonction de Hachage

Pour faire la Hash de nos transaction nous utilisons SHA-256.
Nous avons choisi le SHA-256 car est un algorithme de hachage de sécurité largement utilisé pour protéger les informations sensibles,telles que les mots de passe et les signatures numériques. 
Il est considéré comme sûr car il est difficile de retrouver les données d'origine à partir de leur hachage et de trouver deux entrées qui produisent le même hachage (collision). 
De plus, la taille de 256 bits du hachage garantit une sécurité largement suffisante pour notre API.
