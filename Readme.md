# Python boardgame XML Scrapper

Le projet consiste à récupérer les données présentes sur des collections ainsi que sur les données de jeux de sociétés depuis l'API geekdo.com mis à disposition sous format `.XML`.

## Table des matières

<!-- TOC -->
* [Python boardgame XML Scrapper](#python-boardgame-xml-scrapper)
  * [Table des matières](#table-des-matires)
  * [Librairies externes utilisées](#librairies-externes-utilises)
  * [Ressources utilisées](#ressources-utilises)
  * [Installation du projet en local](#installation-du-projet-en-local)
    * [Création d'un environnement lié au projet](#cration-dun-environnement-li-au-projet)
    * [Activation de l'environnement](#activation-de-lenvironnement)
    * [Installation des librairies et dépendances](#installation-des-librairies-et-dpendances)
  * [Configuration du projet](#configuration-du-projet)
    * [Liste des paramètres](#liste-des-paramtres)
<!-- TOC -->

## Librairies externes utilisées 

| Librairie       | Version  |
|-----------------|----------|
| BeautifulSoup 4 | `4.11.1` |
| Flask           | `2.2.2`  |

Liste des dépendances disponible dans le fichier [requirements.txt](./requirements.txt).

## Ressources utilisées

| Ressource                                                                                                      | Description                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [`https://api.geekdo.com/xmlapi/collection/[:USERNAME]]`](https://api.geekdo.com/xmlapi/collection/megtrinity) | URL prenant un USERNAME en paramètre permettant de récupérer la collection de jeux de sociétés lié au compte spécifié |
| [`https://api.geekdo.com/xmlapi/boardgame/[:ID]`](https://api.geekdo.com/xmlapi/boardgame/275044)              | URL prenant un ID en paramètre permettant de récupérer les données d'un jeu de société en particulier                 |

Les routes vers les différentes ressources ont étés initialisés dans le fichier [routes.py](./src/routes.py)

## Installation du projet en local

### Création d'un environnement lié au projet
```shell
python3 -m venv [NOM_ENVIRONNEMENT]
```

### Activation de l'environnement
```shell
# WINDOWS
[NOM_ENVIRONNEMENT]\Scripts\activate
```

```shell
# MACOS / LINUX -> BASH
[NOM_ENVIRONNEMENT]/bin/activate
```

```shell
# MACOS / LINUX -> ZSH
source [NOM_ENVIRONNEMENT]/bin/activate
```

### Installation des librairies et dépendances
```shell
pip install -r requirements.txt
```

## Configuration du projet
Le projet offre des paramètres configurable que l'on peut adapter selon nos besoins.
Ces derniers peuvent être modifiés dans le fichier [main.py](./main.py).

### Liste des paramètres

| Paramètre                    | Type de donnée | Description                                                                                       |
|------------------------------|----------------|---------------------------------------------------------------------------------------------------|
| `collection_username`        | `String`       | Le nom de l'utilisateur possédant la collection que l'on souhaite récupérer                       |
| `save_locally`               | `Boolean`      | Permet de définir si l'on souhaite sauvegarder localement les données récupérées par le programme |
| `local_collection_file_path` | `String`       | Permet de définir le chemin où sera enregistré les données de la collection                       |
| `local_boardgame_file_path`  | `String`       | Permet de définir le chemin où sera enregistré les données du jeu de société                      |
|                              |                |                                                                                                   |
