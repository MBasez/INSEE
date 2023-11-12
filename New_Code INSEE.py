from tkinter import *

def validation_insee():
    '''Cette fonction permet de confirmer la validation d'un code insee:
    -Elle utilise une condition et une suite arithméthique'''
    # Récupération du Code INSEE saisi dans le champ de texte
    code_insee = Cinsee.get()
    assert len(str(code_insee)) == 15, "Le code insee doit contenir exactement 15 chiffres"
    
    # Vérification de la longueur du Code INSEE qui doit contenir 15 chiffres.
    if 10**14 < int(code_insee) < 10**15:
        # Calcul de la clé de contrôle
        c = (97 - (int(code_insee) // 100) % 97)
        d = int(code_insee) % 100
        
        # Vérification de la clé de contrôle
        if d == c:
            TexteC['text'] = "True"
        else:
            TexteC['text'] = "False"
    else:
        TexteC['text'] = "Votre code doit nécessairement contenir 15 chiffres."

# Création de la fenêtre principale
F = Tk()
F.geometry('1000x500')
F.title('CODE INSEE')
F['bg'] = 'black'
F.resizable(height=False, width=False)

# Création des textes
Texte = Label(F, text='Veuillez saisir votre Code Insee ci-dessous :', font=("Verdana", 15, "italic bold"), fg='white', bg='black')
TexteB = Label(F, text='N oubliez pas d entrer les 15 chiffres du Code Insee', font=('Verdana', 12, 'italic bold'), fg='white', bg='black')
TexteC = Label(F, text='', font=('Verdana', 12, 'italic bold underline'), fg='white', bg='black')

Texte.pack()
TexteB.pack()
TexteC.place(x=260, y=400)

# Création de l'entrée Cinsee et du champ de saisie du Code INSEE
Cinsee = StringVar()
Cinsee_ET = Entry(F, textvariable=Cinsee)
Cinsee_ET.place(x=430, y=200)

# Bouton d'entrée pour appeler la fonction validation_insee
BT = Button(F, text="Entrer", bg='white', fg='black', font=('Verdana', 14, 'bold underline'), command=validation_insee)
BT.pack(side=LEFT, padx=450)

# Lancement de la boucle principale de l'interface graphique
F.mainloop()