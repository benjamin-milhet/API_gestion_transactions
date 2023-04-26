# API de gestion de transactions

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

[![](https://img.shields.io/badge/PROJET_TERMINÉ_🚀-059142?style=for-the-badge&logoColor=white)](https://dev.to/envoy_/150-badges-for-github-pnk) 

[![newPush](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/main.yml/badge.svg)](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/main.yml)
[![curl planete](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/curl.yml/badge.svg)](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/curl.yml)
[![checkSyntax](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/checkSyntax.yml/badge.svg)](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/checkSyntax.yml)
[![Docker Image CI](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/docker-image.yml/badge.svg)](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/docker-image.yml)
[![Docker push GCR](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/Docker_push_GCR.yml/badge.svg)](https://github.com/benjamin-milhet/API_gestion_transactions/actions/workflows/Docker_push_GCR.yml)

## Membres du groupe
 - Clément GHYS
 - Benjamin MILHET
 
## ILC
 
## Fonctionnalités:
Cette API développée en python a pour but de pouvoir gérer des transactions entre des personnes. 

 - Enregistrer une transaction.
 - Afficher une liste de toutes les transactions dans l’ordre chronologique.
 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
 - Afficher le solde du compte de la personne.
 - Importer des données depuis un fichier csv.
 - Vérification des transactions grâce à un hashage SHA-256


## Langage
Pour réaliser notre API, nous allons utiliser le langage Python avec le framework Flask permettant le dévelopement web avec Python. L'objectif de notre API est réaliser un système de transaction d'argent entre deux personnes.

## Documentation

 - [Fichier Swagger](https://github.com/benjamin-milhet/API_gestion_transactions/blob/main/swagger.yaml)
 - [Documentation de la classe Personne](https://github.com/benjamin-milhet/API_gestion_transactions/blob/main/Readme-Personne.md)
 - [Documentation du dockerfile](https://github.com/benjamin-milhet/API_gestion_transactions/blob/main/Readme-Dockerfile.md)
 - [Documentation du chargement des fichiers](https://github.com/benjamin-milhet/API_gestion_transactions/blob/main/Readme-chargerFichier.md)
 - [Documentation du hachage](https://github.com/benjamin-milhet/API_gestion_transactions/blob/main/Readme-Hash.md) 

## Exemples requêtes CURL
```
 - Charger deux fichiers CSV : curl -X POST -d "fichierPersonne=data.csv" -d "fichierTransaction=transactions.csv"  -d "delimiter=;" http://127.0.0.1:5000/chargerFichier
 - Ajouter une transaction : curl -X POST -d "P1=Lucas" -d "P2=Benjamin" -d "s=10" http://127.0.0.1:5000/addTransaction
 - Récupérer les transactions : curl -X GET  http://127.0.0.1:5000/getTransactions
 - Récupérer les informations d'une personne avec ses transactions : curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getPersonne
 - Récupérer le solde d'une personne : curl -X GET -d "nom=Benjamin"  http://127.0.0.1:5000/getSoldePersonne
 - Vérifier le hashage des transactions existentes : curl -X GET http://127.0.0.1:5000/verifierTransaction
```


[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)


