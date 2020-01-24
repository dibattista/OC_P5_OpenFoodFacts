from GUI.selectApiData import SelectApi
import tkinter as tk
from tkinter import font as tkfont

import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_geometry("1000x1200")
        self.title('Pur Beurre')
        

        self.title_font = tkfont.Font(family='Helvetica', size=22, weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("PageOne")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.lift()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#bfbfbf')
        # label = tk.Label(self, text="Choisissez ce que vous voulez faire.",
        #                 font=controller.title_font)
        # label.pack(side="top", ipady=30, pady=10, )

        button1 = tk.Button(
            self, text="1- Remplacer un aliment.", command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(
            self, text="2- Retrouver mes aliments substitués.", command=lambda: controller.show_frame("PageFive"))

        button1.config(font='Helvetica 14', height=5, width=40)
        button2.config(font='Helvetica 14', height=5, width=40)
        button1.place(x=335, y=250)
        button2.place(x=335, y=400)
        


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        self.get_categories = self.api_select.get_categories()
        self.val = '1'

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="This is Page 2",
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=150)

        def get_val():
            print('how to send v.get() tp P3?',  v.get())

        # choose categories
        v = tk.StringVar()

        for value in self.get_categories:
            r1 = tk.Radiobutton(self, text=value[1], variable=v, value=value[0], indicator=0,
                                background="light blue", command=lambda: [get_val(), controller.show_frame("PageThree")])
            r1.pack(fill=tk.X, padx=200)
        
        button = tk.Button(self, text="Go back",
                        command=lambda: controller.show_frame("PageOne"))
        button.pack(fill=tk.X, padx=200)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        # TO DO !!!! - recupérer la value '1' categorie
        self.get_aliment = self.api_select.get_aliment('1')

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="This is Page 3",
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)

        label_2 = tk.Label(self, text="Comment récupérer la value de P2????")
        label_2.pack()

        v = tk.StringVar()

        for value in self.get_aliment:
                    r1 = tk.Radiobutton(self, text=value[1], variable=v, value=value[0], indicator=0,
                                        background="light blue", command=lambda: controller.show_frame("PageFour"))
                    r1.pack(fill=tk.X, padx=200)

        button = tk.Button(self, text="Go back",
                        command=lambda: controller.show_frame("PageTwo"))
        button.pack()


class PageFour(tk.Frame):
    def __init__(self, parent, controller, rows=10, columns=2):
        self.api_select = SelectApi()
        # TO DO !!!! - ici change le '1' par aliment_choose
        # TO DO !!!! - il faut la categorie aussi
        categorie = '1'
        nutri_grade = self.api_select.get_nutrition_grade('1')
        substitu = self.api_select.get_substitute_aliment(
            categorie, nutri_grade)

        # TO DO !!!! - comment je veut afficher substitu
        # (5, 'Ligne gourmande', 'Magasins U, Carrefour', 'https://world.openfoodfacts.org/product/3664346306621/ligne-gourmande-poulain')
        # TO DO !!!! - faire une commande sauvegarde pour le boutton_1 avec dans la fonction
        #             self.api_select.backup_substitute(substitu)

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        container_P4 = tk.Frame(self)
        container_P4.pack(pady=200)
        container_P4.grid_rowconfigure(0, weight=1)
        container_P4.grid_columnconfigure(0, weight=1)

        var_5 = tk.StringVar()
        var_6 = tk.StringVar()
        var_7 = tk.StringVar()
        var_8 = tk.StringVar()

        label_title = tk.Label(container_P4, text="Voici le produit avec le meuilleur nutri-store", width="40", height="3")
        label_1 = tk.Label(container_P4, text="Nom du produit",
                        relief="solid", width="40", height="3")
        label_2 = tk.Label(container_P4, text="Magasin",
                        relief="solid", width="40", height="3")
        label_3 = tk.Label(container_P4, text="Lien vers Openfoodfact",
                        relief="solid", width="40", height="3")
        label_4 = tk.Label(container_P4, text="Nutri-scrore",
                        relief="solid", width="40", height="3")
        label_5 = tk.Label(container_P4, textvariable=var_5,
                        relief="solid", width="40", height="3")
        label_6 = tk.Label(container_P4, textvariable=var_6,
                        relief="solid", width="40", height="3")
        label_7 = tk.Label(container_P4, textvariable=var_7,
                        relief="solid", width="40", height="3")
        label_8 = tk.Label(container_P4, textvariable=var_8,
                        relief="solid", width="40", height="3")

        label_title.grid()
        label_1.grid(row=0, column=0)
        label_2.grid(row=1, column=0)
        label_3.grid(row=2, column=0)
        label_4.grid(row=3, column=0)
        label_5.grid(row=0, column=1)
        label_6.grid(row=1, column=1)
        label_7.grid(row=2, column=1)
        label_8.grid(row=3, column=1)

        var_5.set(substitu[1])
        var_6.set(substitu[2])
        var_7.set(substitu[3])
        var_8.set(substitu[4])




class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        list_aliment_id = self.api_select.get_all_substitute()
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is Page 5",
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # TO DO !!!! - comment j'affiche la liste ????
        for id in list_aliment_id:
                self.api_select.get_aliment_substitute(id[0])



class Window:
    def __init__(self):
        app = MainPage()
        app.mainloop()


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
