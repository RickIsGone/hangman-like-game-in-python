from random_word import RandomWords
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import *  
import pygame


pygame.mixer.init()
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.set_volume(0.1) 
pygame.mixer.music.play(start=10.3,loops=-1)             # faccio partire il suono


#random_word="cyka"                  debug
r = RandomWords()                                                                       # non mi ricordo 
random_word = r.get_random_word()                                                       # generazione parola
word_state = [random_word[0]] +['_' for _ in random_word[1:-1]]+[random_word[-1]]       # inizializzazione con iniziale e finale e _




                                                                                        # inizializzazione gui                           




finestra = tk.Tk()                                 # generazione finestra
finestra.geometry("1920x1080")                     # Imposta le dimensioni della finestra a 1920x1080
finestra.title("impiccato")                        # Imposta il titolo della finestra
finestra.config(bg='#1E1E1E')                      # imposto il colore dello sfondo su grigio scuro

canvas=Canvas(finestra,width=500,height=500,bg='#1E1E1E',highlightthickness=0)              # creo uno spazio nella finestra 
canvas.pack()                                                                               # lo posiziono 
img=PhotoImage(file='fasi/i0.png')                                                          # gli dico che file prendere 
image_on_canvas=canvas.create_image(310,310,image=img)                                      # dico che parte dell'immagine prendere 
canvas.place(relx=0.75,rely=0.4,anchor='center')                                            # gli do delle cordinate 


parola = tk.Label(finestra, text=" ".join(word_state), font=("calibri", 48),bg='#1E1E1E',fg='white')                # dichiarazioone parola 
parola.pack()                                                                                                       # posizionamento parola nella finestra 
parola.place(relx=0.2, rely=0.5, anchor='center')                                                                   # dichiarazione posizione 


lives=10                                                                                                            # dichiarazione vite 
vite=tk.Label(finestra,text=f"vite rimaste: {lives}", font=("calibri", 30),bg='#1E1E1E',fg='white')                 # dichiarazione nella finestra 
vite.pack()                                                                                                         # posizionamento nella finestra 
vite.place(relx=0.3)                                                                                                # dichiarazione posizione 


indovinate=0
indo=tk.Label(finestra,text=f"parole indovinate: {indovinate}", font=("calibri", 30),bg='#1E1E1E',fg='white')                  # dichiarazione nella finestra 
indo.pack()
indo.place(relx=0.6)


lettera=tk.Entry(finestra,width=15,font=("calibri",24))                                 # creazione finestra input 
lettera.pack()                                                                          # posizionamento nella finesta 
lettera.place(relx=0.45, rely=0.8)                                                      # dichiarazione posizione 


domanda=tk.Label(finestra,text='do you want to guess the word or a letter? (w/l)',font=("calibri", 30),bg='#1E1E1E',fg='white')         # creo la domanda 
domanda.pack()                                                                                                                          # posizionamento nella finestra 
domanda.place(relx=0.52, rely=0.75,anchor='center')                                                                                     # dichiazione posizione 




                                                                                    # inizio funzioni  




def reset():
    global random_word, word_state, lives, img, lettera_in,indovinate
    random_word = r.get_random_word()
    word_state = [random_word[0]] + ['_' for _ in random_word[1:-1]] + [random_word[-1]]
    lives = 10
    img = PhotoImage(file='fasi/i0.png')
    canvas.itemconfig(image_on_canvas, image=img)                                               # creo una funzione che restarta il gioco, distrugge il pulsante e aumenta di uno le parole indovinate 
    lettera_in = ''
    parola.config(text=" ".join(word_state))
    vite.config(text=f"vite rimaste:{lives}")
    domanda.config(text='do you want to guess the word or a letter? (w/l)')
    invio.config(command=get_scelta)
    pulreset.destroy()
    indovinate+=1
    indo.config(text=f'parole indovinate: {indovinate}')


def bottone():
    global pulreset
    pulreset=tk.Button(finestra,text='reset',command=reset)                        # creo un bottone che quando schiacciato fa partire la funzione reset
    pulreset.pack()                                                                # metto il bottone sulla finestra
    pulreset.place(relx=0.58, rely=0.77)                                           # gli do una posizione nella finestra 
    

def get_scelta():                                       # creo la funzione che prende la scelta dell'utente 
    global lettera_in                                   # metto lettera_in come parametro globale 
    lettera_in = lettera.get()                          # assegno alla variabile lettera_in la lettera nella casella di input
    lettera.delete(0,tk.END)                            # cancello la casella di input
    if lettera_in!='l' and lettera_in!='w':
        domanda.config(text='thats not and option, do you want to guess the word or a letter? (w/l)')
        lettera.delete(0,tk.END)                        # cancello la casella di input
        invio.config(command=get_scelta) 
    elif lettera_in == 'l':                                
        domanda.config(text='guess a letter')           # cambio la scritta 
        invio.config(command=get_lettera)               # se il pulsante viente schiacciato e la lettera inserita è la l il programma va alla funzione get_lettera
    else:                                               
        domanda.config(text='guess the word')           # cambio la scritta 
        invio.config(command=get_parola)                # se il pulsante viente schiacciato e la lettera inserita è la l il programma va alla funzione get_parola


def get_lettera():                                                                                                  # creo la funzione che gestisce l'input delle lettere 
    global lettera_in, lives, word_state                                                                            # metto word_state,lives e lettera_in come parametri globali 
    lettera_in = lettera.get()                                                                                      # assegno alla variabile lettera_in la lettera nella casella di input
    if lettera_in in random_word:                                                                                   # controllo se la lettera è nella parola 
        domanda.config(text='you guessed a letter, do you want to guess the word or a letter? (w/l)')               # cambio la domanda 
        lettera.delete(0,tk.END)                                                                                    # cancello la casella di input
        for i, letter in enumerate(random_word):                                                                    # per ogni lettera nella parola do un valore ad essa
            if letter == lettera_in:                                                                                
                word_state[i] = letter                                                                              # cambio la variabile aggiungendo le lettere scoperte nella loro posizione 
        parola.config(text=" ".join(word_state))                                                                    # aggiorno la parola visibile 
        if ("".join(word_state))==random_word:                                                                      # controlla se le lettere indovinate sono uguali alla parola 
            domanda.config(text='you guessed the word, congratulation')                                             # cambio il testo  
            parola.config(text=random_word)                                                                         # aggiorno la parola visibile con la parola completa 
            bottone()                                                                                               # fa partire la funzione bottone
    else:
        lives -= 1                                                                                                  # diminuisco le vite di uno 
        domanda.config(text='the letter is not in the word, do you want to guess the word or a letter? (w/l) ')     # cambio la domanda 
        lettera.delete(0,tk.END)                                                                                    # cancello la casella di input
        vite.config(text=f"vite rimaste:{lives}")                                                                   # aggiorno il counter delle vite 
    invio.config(command=get_scelta)                                                                                # se il pulsante viene schiacciato fa partire la funzione get_scelta


def get_parola():                                                           # dichiaro la funzione 
    global lettera_in, lives,img                                            # dichiaro lettera_in e lives come puntatori globali 
    lettera_in = lettera.get()                                              # assegno a lettera_in la parola nella casella di input
    if lettera_in == random_word:                                           
        domanda.config(text='you guessed the word, congratulation')         # cambio il testo 
        lettera.delete(0,tk.END)                                            # cancello la casella di input 
        parola.config(text=random_word)                                     # aggiorno la parola visibile con la parola completa
        bottone()                                                           # fa partire la funzione bottone     
    else:
        lives = 0                                                           # metto a 0 le vite 
        domanda.config(text='the word was not correct')                     # aggiorno il testo 
        lettera.delete(0,tk.END)                                            # cancello la casella di input
        img = PhotoImage(file='fasi/i10.png')                               # cambia l'immagine 
        canvas.itemconfig(image_on_canvas,image=img)                        # aggiorna l'immagine 
    vite.config(text=f"vite rimaste: {lives}")                              # aggiorno il counter delle vite a 0 

 
invio = tk.Button(finestra, text='invio', command=get_scelta)               # creo un bottone che quando schiacciato fa partire la funzione get_scelta 
invio.pack()                                                                # metto il bottone sulla finestra
invio.place(relx=0.58, rely=0.807)                                          # gli do una posizione nella finestra 


def i_am_become_death_the_destroyer_of_worlds():                            # dichiaro la funzione 
    finestra.destroy()                                                      # chiude la finestra 


def check():                                                                # dichiaro la funzione 
    global img                                                              # dichiaro img come puntatore glbale 
    if lives == 0:                                                          
        domanda.config(text='the word was ' + ''.join(random_word))         # do in output la parola 
        img = PhotoImage(file='fasi/i10.png')                               # cambio l'immagine 
        canvas.itemconfig(image_on_canvas,image=img)                        # aggiorno l'immagine 
        finestra.after(6000,i_am_become_death_the_destroyer_of_worlds)      # metto in attesa di 6 secondi una fuznione 
    elif lives>0:
        if lives==9:
            img=PhotoImage(file='fasi/i1.png')
        elif lives==8:
            img=PhotoImage(file='fasi/i2.png')
        elif lives==7:
            img=PhotoImage(file='fasi/i3.png')
        elif lives==6:
            img=PhotoImage(file='fasi/i4.png')
        elif lives == 5:
            img = PhotoImage(file='fasi/i5.png')                            # in base alle vite rimaste cambia l'immagine 
        elif lives == 4:
            img = PhotoImage(file='fasi/i6.png')
        elif lives == 3:
            img = PhotoImage(file='fasi/i7.png')
        elif lives == 2:
            img = PhotoImage(file='fasi/i8.png')
        elif lives == 1:
            img = PhotoImage(file='fasi/i9.png')
        canvas.itemconfig(image_on_canvas,image=img)                        # aggiorno l'immagine 
        finestra.after(100,check)                                           # fa ripartire la funzione check ogni centesimo 


check()                     # fa partire la funzione check
finestra.mainloop()         # comando per far funzionare il programma                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ammazzatemi, ho passato troppo tempo inutilmente su questo programma 