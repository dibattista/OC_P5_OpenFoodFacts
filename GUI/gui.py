# coding=utf-8

from GUI.selectApiData import SelectApi
import tkinter as tk
from tkinter import font as tkfont

import os
import webbrowser


var_categorie = '0'
var_aliment = '0'
var_all_substitue = []

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_geometry("1000x1200")
        self.title('Ratatouille')

        self.title_font = tkfont.Font(family='Helvetica', size=22, weight="bold")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        #print('self.frames IN MAIN PAGE', self.frames)
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
        def refresh():
            frame = PageFive(parent=controller.container,
                            controller=controller)
            controller.frames["PageFive"] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        button1 = tk.Button(
            self, text="1- Quel aliment souhaitez-vous remplacer?", command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(
            self, text="2- Retrouver mes aliments substitués.", command=lambda: [refresh(), controller.show_frame("PageFive")])

        button1.config(font='Helvetica 14', height=5, width=40)
        button2.config(font='Helvetica 14', height=5, width=40)
        button1.place(x=335, y=250)
        button2.place(x=335, y=400)
        


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        self.get_categories = self.api_select.get_categories()

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="Sélectionnez la catégorie",
                        bg='#f0f0f0', font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        v = tk.StringVar()

        def get_val():
            global var_categorie
            var_categorie = v.get()

            #### ici on update la page 3
            frame = PageThree(parent=controller.container,
                            controller=controller)
            controller.frames["PageThree"] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # choose categories

        for value in self.get_categories:
            r1 = tk.Radiobutton(self, text=value[1], variable=v, value=value[0], indicator=0, width="40", height="2",
                                background="light blue", command=lambda: [get_val(), controller.show_frame("PageThree")])
            r1.pack()
        
        button = tk.Button(self, text="Revenir à l'accueil", width="40", height="2",
                        command=lambda: controller.show_frame("PageOne"))
        button.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        self.get_aliment = self.api_select.get_aliment(var_categorie)

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="Sélectionnez l'aliment",
                        bg='#f0f0f0', font=controller.title_font)
        label.pack(side="top", fill="x", pady=80)

        v = tk.StringVar()

        def get_val():
            global var_aliment
            var_aliment = v.get()

            #### ici on update la page 3
            frame = PageFour(parent=controller.container,
                            controller=controller)
            controller.frames["PageFour"] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        for value in self.get_aliment:
            #print('value in for P3', value)
            r1 = tk.Radiobutton(self, text=value[1], variable=v, value=value[0], indicator=0, width="35", height="1",
                                background="light blue",
                            command=lambda: [get_val(), controller.show_frame("PageFour")])
            r1.pack()

        button = tk.Button(self, text="Revenir",  width="35", height="1",
                        command=lambda: controller.show_frame("PageTwo"))
        button.pack()


class PageFour(tk.Frame):
    def __init__(self, parent, controller, rows=10, columns=2):
        self.api_select = SelectApi()
        self.categorie = var_categorie
        self.nutri_grade = self.api_select.get_nutrition_grade(var_aliment)
        substitue = [None] * 5
        subs = self.api_select.get_substitute_aliment(
            self.categorie, self.nutri_grade)
                
        for s in subs:
            substitue = s

        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="Un aliment plus sain", bg='#f0f0f0',
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)

        def open_url():
            webbrowser.open_new(substitue[3])
            
        def backup_substitue():
            if backup_button["text"] == "Sauvegarder":
                self.api_select.backup_substitute(substitue[0])

                # change text button
                backup_button["text"] = "C'est sauvegarder"
            else:
                backup_button["text"] = "Sauvegarder"


        container_P4 = tk.Frame(self)
        container_P4.pack()
        container_P4.grid_rowconfigure(0, weight=1)
        container_P4.grid_columnconfigure(0, weight=1)

        var_4 = tk.StringVar()
        var_5 = tk.StringVar()
        var_6 = tk.StringVar()

        label_title = tk.Label(container_P4, text="Voici le produit avec le meuilleur nutri-store", width="40", height="3")
        label_1 = tk.Label(container_P4, text="Nom du produit",
                        relief="solid", width="40", height="3")
        label_2 = tk.Label(container_P4, text="Magasin",
                        relief="solid", width="40", height="3")
        label_3 = tk.Label(container_P4, text="Nutri-scrore",
                        relief="solid", width="40", height="3")
        label_4 = tk.Label(container_P4, textvariable=var_4,
                        relief="solid", width="40", height="3")
        label_5 = tk.Label(container_P4, textvariable=var_5,
                        relief="solid", width="40", height="3")
        label_6 = tk.Label(container_P4, textvariable=var_6,
                        relief="solid", width="40", height="3")

        label_title.grid()
        label_1.grid(row=0, column=0)
        label_2.grid(row=1, column=0)
        label_3.grid(row=2, column=0)
        label_4.grid(row=0, column=1)
        label_5.grid(row=1, column=1)
        label_6.grid(row=2, column=1)

        var_4.set(substitue[1])
        var_5.set(substitue[2])
        var_6.set(substitue[4])

        link_button = tk.Button(self, text="Lien vers Open Food Fact",
                                relief="solid", width="81", height="3", command=open_url)
        link_button.pack()

        backup_button = tk.Button(self, text="Sauvegarder", background="light blue",
                                relief="solid", width="81", height="3", command=backup_substitue)
        backup_button.pack()

        back_button = tk.Button(self, text="Revenir à l'accueil", width="81", height="3", background="light blue",
                                command=lambda: controller.show_frame("PageOne"))
        back_button.pack()




class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        self.api_select = SelectApi()
        var_all_substitue = []

        #list_aliment_id = self.api_select.get_all_substitute()
        
        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        label = tk.Label(self, text="Liste des aliments aux meuilleurs grade", bg='#f0f0f0',
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)

        self.container_P5 = tk.Frame(self)
        self.container_P5.pack()
        self.container_P5.grid_rowconfigure(0, weight=1)
        self.container_P5.grid_columnconfigure(0, weight=1)
        
        # TO DO !!!! - comment j'affiche la liste ????
        label_name = tk.Label(self.container_P5, text='Nom', width=40,
                        relief="solid")
        label_name.grid(row=0, column=0)

        label_shop = tk.Label(self.container_P5, text='Magasin', width=40,
                            relief="solid")
        label_shop.grid(row=0, column=1)

        label_grade = tk.Label(self.container_P5, text='Grade', width=30,
                            relief="solid")
        label_grade.grid(row=0, column=2)

        list_aliment_id = self.api_select.get_all_substitute()
        for id in list_aliment_id:
            all_aliment = self.api_select.get_aliment_substitute(id)
            var_all_substitue.append(all_aliment)
        
        for row_index, val in enumerate(var_all_substitue):
            #print('row', row)
            for cell in val:
                label_1 = tk.Label(self.container_P5, text=cell[1], width=40,
                                relief="solid")
                label_1.grid(row=row_index +1, column=0)

                label_2 = tk.Label(self.container_P5, text=cell[2], width=40,
                                relief="solid")
                label_2.grid(row=row_index +1, column=1)

                label_4 = tk.Label(self.container_P5, text=cell[4], width=30,
                                relief="solid")
                label_4.grid(row=row_index +1, column=2)



        button = tk.Button(self, text="Go back", width=40,
                        command=lambda: controller.show_frame("PageOne"))
        button.pack(pady=40)





class Window:
    def __init__(self):
        app = MainPage()
        app.mainloop()
