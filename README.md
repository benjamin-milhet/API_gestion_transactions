# GHYS_MILHET_4A_ILC_WORKFLOW

## Membres du groupe
 - Clément GHYS
 - Benjamin MILHET
 
## ILC

## Langage
Pour réaliser notre API, nous allons utiliser le langage Python avec le framework Flask permettant le dévelopement web avec Python. L'objectif de notre API est réaliser un système de transaction d'argent entre deux personnes.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

[![newPush](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC/actions/workflows/main.yml/badge.svg)](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC/actions/workflows/main.yml)
[![curl planete](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC/actions/workflows/curl.yml/badge.svg)](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC/actions/workflows/curl.yml)
[![checkSyntax](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/checkSyntax.yml/badge.svg)](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/checkSyntax.yml)
[![Docker Image CI](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/docker-image.yml/badge.svg)](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/docker-image.yml)
[![Docker push GCR](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/Docker_push_GCR.yml/badge.svg)](https://github.com/benjamin-milhet/GHYS_MILHET_4A_ILC_WORKFLOW/actions/workflows/Docker_push_GCR.yml)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

# API de gestion de transactions
Cette API développée en python a pour but de pouvoir gérer des transactions entre des personnes. ### Fonctionnalités:
 - Enregistrer une transaction.
 - Afficher une liste de toutes les transactions dans l’ordre chronologique.
 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
 - Afficher le solde du compte de la personne.
 - Importer des données depuis un fichier csv.

## Version: v1.0.0

### /

#### GET
##### Summary:

Accueil

##### Description:

Retourne "Hello, world!"

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | string |

### /getTransactions

#### GET
##### Summary:

Récupérer les transactions

##### Description:

Retourne les transactions classées par date

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | string |

### /addTransaction

#### POST
##### Summary:

Ajouter une transaction

##### Description:

Ajouter une transaction entre deux personnes avec un solde donné

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| P1 | formData | Nom de la première personne | Yes | string |
| P2 | formData | Nom de la deuxième personne | Yes | string |
| s | formData | Solde de la transaction | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | string |

### /chargerFichier

#### POST
##### Summary:

Charger un fichier

##### Description:

Charger un fichier CSV contenant les informations des personnes

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| fichier | formData | Nom du fichier | Yes | string |
| delimiter | formData | Délimiteur utilisé dans le fichier | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | string |

### /getPersonne

#### GET
##### Summary:

Récupérer les informations d'une personne

##### Description:

Récupérer les transactions d'une personne en fonction de son nom

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| nom | formData | Nom de la personne | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | string |

### /getSoldePersonne

#### GET
##### Summary:

Récupérer le solde d'une personne

##### Description:

Récupérer le solde d'une personne en fonction de son nom

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| nom | formData | Nom de la personne | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Succès | integer |

