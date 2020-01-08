## utiliser ici tkinter

from InteractionUser.selectApi import SelectApi

class StartInteraction:
    api_select = SelectApi()

    first_question = input("1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués.")

    if first_question == "1":
        categorie = input(api_select.get_categories())
        aliment_choose = input(api_select.get_aliment(categorie))
        nutri_grade = api_select.get_nutrition_grade(aliment_choose)
        ## print('nutri_grade in p5', nutri_grade)
        substitu = api_select.get_substitute_aliment(categorie, nutri_grade)
        print(' This is the result of your substitute:')
        print(substitu)
        api_select.backup_substitute(substitu)


    elif first_question == "2":
        print("Voici la liste de vos alliment sauvegarder")
        list_aliment_id = api_select.get_all_substitute()
        for id in list_aliment_id:
            api_select.get_aliment_substitute(id[0])
    else:
        input("1 ?, 2 Retrouver mes aliments substitus.")