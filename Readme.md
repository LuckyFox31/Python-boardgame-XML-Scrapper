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
<!-- TOC -->

## Librairies externes utilisées 

| Librairie       | Version  |
|-----------------|----------|
| BeautifulSoup 4 | `4.11.1` |
| Flask           | `2.2.2`  |

Liste des dépendances disponible dans le fichier [requirements.txt](./requirements.txt).

## Ressources utilisées

| Ressource                                                                                                    | Description                                                                                           |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [`https://api.geekdo.com/xmlapi/collection/megtrinity`](https://api.geekdo.com/xmlapi/collection/megtrinity) | URL vers la collection de jeux de sociétés lié au compte intitulé **megtrinity**                      |
| [`https://api.geekdo.com/xmlapi/boardgame/[:ID]`](https://api.geekdo.com/xmlapi/boardgame/275044)            | URL prenant un ID en paramètre permettant de récupérer les données d'un jeu de société en particulier |

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
