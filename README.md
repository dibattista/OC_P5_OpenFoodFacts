# OC_P5_OpenFoodFacts

Open Food Facts est une base de données sur les produits alimentaires, incrémenter par tous les utilisateurs du monde entier.

Ce projet interagirait avec cette l'API d'Open Food Facts en français pour récupérer les aliments et leurs propriétés, comme le grade qui vat permettre au programme de proposer un aliment plus sain.

## User features

Pour utiliser ce programme vous avez besoin de créer une nouvelle base de données pour y insérer les data de l'api qui sont récupérer et netoyer pour vous.

Dans votre terminal vous pourrez donc lancé la création de la db de ces tables et insertons des données en un click.

Une fois que vous aurez vérifier que la base de données est bien remplit vous pourez lancé les programme.

Dans la première page deux boutons vous donnerons le choix :
    1 - Sélectionner un aliment a remplacé.
    2 - Retrouver ses aliments substitués.

la deuxème page permet de choisir une catégorie
la troisième page de choisir un aliment de cette catégorie
la quatrième page:
    de voir l'alliment le plus sain pour cette catégorie
    de ce diriger vers la page open food fact du produit
    de sauvegarder ce resultat
    et de revenir a la première page

Dans la cinquième page qui souvre grace au deuxième bouton de la page 1, vous trouverez le tableau
des résulats enregistrer dans la page quatre.

## Prerequistes

* Python3.6
* MySql

## Dependance

* mysql-connector
* Requests
* prettytable

## Setup

Add variable environment with this command line:
```export YOUR_HOST='YOUR HOST'```
```export NAME_DATABASE='YOUR DATABASE NAME'```
```export USER_NAME='YOUR USER NAME'```
```export PASSWORD_DATABASE='YOUR DATEBASE PASSWORD'```

## Launch development

For launch the script to create the database:

```python main.py -n```

For launch the project:

```python main.py```
