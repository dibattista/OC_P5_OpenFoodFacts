from BetterFood.selectApiData import SelectApi
import tkinter as tk

import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

    
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        ##????? cela créer une nouvelle fenêtre pour le checkbutton comment faire pour rester dans la meme page?:
        self.api_select = SelectApi()
        # self ou pas self?
        self.get_categories = self.api_select.get_categories()

        #Page.__init__(self, *args, **kwargs)
        
        ## comment revenir a la page d'avant?

        ###############################  Radiobutton
        # est-ce que ce tk frame suprime le main?
        tk.Frame.__init__(self, *args, **kwargs)
        label = tk.Label(
            self, text="P1 - Choose a number from a categories list")
        label.pack(side="top", fill="both", expand=False)
        def open_p3():
            print('in p3', v.get())
        p3 = Page3(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        v = tk.StringVar()

        for text, value in self.get_categories:
            tk.Radiobutton(self, text=value, variable=v, value=value, indicator=0,
                        background="light blue", command=lambda: open_p3()).pack(side="top", fill="both")

        ################################ END  Radiobutton

class Page2(Page):
    def __init__(self, *args, **kwargs):
            Page.__init__(self, *args, **kwargs)
            label = tk.Label(self, text="This is page 2")
            label.pack(side="top", fill="both", expand=True)


class Page3(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class MainPage(tk.Frame):
    # test tkinter
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        #buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        #buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_= container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1 = tk.Button(
            self, text="1- Remplacer un aliment.", command=p1.lift)
        b2 = tk.Button(
            self, text="2- Retrouver mes aliments substitués.", command=p2.lift)

        b1.place(x=150, y=250)
        b2.place(x=350, y=250)





class Window:
    def __init__(self):
        root = tk.Tk()
        self.api_select = SelectApi()
        # self ou pas self?
        self.get_categories = self.api_select.get_categories()

        main = MainPage(root)
        main.pack(side="top", fill="both", expand=True)
        root.wm_geometry("800x600")
        root.mainloop()


class BetterFood:
    def __init__(self):
        self.api_select = SelectApi()
    
    def startFinding(self):
        first_question = input(
            "1- Quel aliment souhaitez-vous remplacer ?, 2- Retrouver mes aliments substitués.")
        
        if first_question == "1":
            categorie = input(self.api_select.get_categories())
            aliment_choose = input(self.api_select.get_aliment(categorie))
            nutri_grade = self.api_select.get_nutrition_grade(aliment_choose)
            ## print('nutri_grade in p5', nutri_grade)
            substitu = self.api_select.get_substitute_aliment(
                categorie, nutri_grade)
            print(' This is the result of your substitute:')
            print(substitu)
            self.api_select.backup_substitute(substitu)

        elif first_question == "2":
            print("Voici la liste de vos alliment sauvegarder")
            list_aliment_id = self.api_select.get_all_substitute()
            for id in list_aliment_id:
                self.api_select.get_aliment_substitute(id[0])
        else:
            input("1 ?, 2 Retrouver mes aliments substitus.")
