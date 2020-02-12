# OC_P5_OpenFoodFacts

Open Food Facts is a food product database, incremented by all users around the world.

This project interacts with this API of Open Food Facts to recover French foods and their properties, such as the grade that will allow the program to offer a healthier food.

## User features

To use this program you need to create a new database to insert the data from the openfoodfact API which is retrieved and cleaned for you.
Once you have verified that the database is full you can launch the programs.

In the first page of the graphical interface two buttons will give you the choice:
    1 - Select a food substitute.
    2 - Find your substituted foods.

the second page allows you to choose a category.
the third page to choose a food from this category.
the fourth page:
    * to see the healthiest food for this category
    * to go to the open food fact page of the product
    * save this result
    * and go back to the first page

In the fifth page that opens with the second button on page 1, you will find the table
results save in page four.

## Prerequistes

You need to have installed:

* Python3.6
* MySql

## Dependance

* mysql-connector
* Requests
* tkinter

## Setup

git clone https://github.com/dibattista/OC_P5_OpenFoodFacts.git

If is not done yet add dependance with: `pip install -r requirements.txt`

Create a Mysql user who has the rights to create a database.

Add variable environment with this command line:<br />
```export YOUR_HOST='YOUR HOST'```<br />
```export NAME_DATABASE='YOUR DATABASE NAME'```<br />
```export USER_NAME='YOUR USER NAME'```<br />
```export PASSWORD_DATABASE='YOUR DATEBASE PASSWORD'```<br />

## Launch development

Like I say before you can create a new database with the tables and datas in one commande line:

```python main.py -n```

After you check your data you can launch the project:

```python main.py```
