from random_word import RandomWords
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import *  
import pygame

# music 
pygame.mixer.init()
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.set_volume(0.1) 
pygame.mixer.music.play(start=10.3,loops=-1)             


#random_word="cyka"                  debug
# generation of the world 
r = RandomWords()                                                                       
random_word = r.get_random_word()                                                       
word_state = [random_word[0]] +['_' for _ in random_word[1:-1]]+[random_word[-1]]      




                                                                                       # gui initialization                           



# window generation 
finestra = tk.Tk()                                 
finestra.geometry("1920x1080")                     
finestra.title("impiccato")                        
finestra.config(bg='#1E1E1E')                      

# creation image
canvas=Canvas(finestra,width=500,height=500,bg='#1E1E1E',highlightthickness=0)             
canvas.pack()                                                                              
img=PhotoImage(file='fasi/i0.png')                                                     
image_on_canvas=canvas.create_image(310,310,image=img)                                     
canvas.place(relx=0.75,rely=0.4,anchor='center')                                            

# putting the world on the screen 
parola = tk.Label(finestra, text=" ".join(word_state), font=("calibri", 48),bg='#1E1E1E',fg='white')                
parola.pack()                                                                                                       
parola.place(relx=0.2, rely=0.5, anchor='center')                                                                  

# initialization lives 
lives=10                                                                                                            
vite=tk.Label(finestra,text=f"{lives} lives left", font=("calibri", 30),bg='#1E1E1E',fg='white')                 
vite.pack()                                                                                                         
vite.place(relx=0.3)                                                                                                

# number of guessed world 
indovinate=0
indo=tk.Label(finestra,text=f"{indovinate} worlds guessed", font=("calibri", 30),bg='#1E1E1E',fg='white')                  
indo.pack()
indo.place(relx=0.6)

# input 
lettera=tk.Entry(finestra,width=15,font=("calibri",24))                                 
lettera.pack()                                                                          
lettera.place(relx=0.45, rely=0.8)                                                      

# question 
domanda=tk.Label(finestra,text='do you want to guess the word or a letter? (w/l)',font=("calibri", 30),bg='#1E1E1E',fg='white')         
domanda.pack()                                                                                                                          
domanda.place(relx=0.52, rely=0.75,anchor='center')                                                                                    




                                                                                    # start of functions   



# restart the game 
def reset():
    global random_word, word_state, lives, img, lettera_in,indovinate
    random_word = r.get_random_word()
    word_state = [random_word[0]] + ['_' for _ in random_word[1:-1]] + [random_word[-1]]
    lives = 10
    img = PhotoImage(file='fasi/i0.png')
    canvas.itemconfig(image_on_canvas, image=img)                                                
    lettera_in = ''
    parola.config(text=" ".join(word_state))
    vite.config(text=f"vite rimaste:{lives}")
    domanda.config(text='do you want to guess the word or a letter? (w/l)')
    invio.config(command=get_scelta)
    pulreset.destroy()
    indovinate+=1
    indo.config(text=f"{indovinate} worlds guessed")

# creates the button to restart the game 
def bottone():
    global pulreset
    pulreset=tk.Button(finestra,text='reset',command=reset)                        
    pulreset.pack()                                                                
    pulreset.place(relx=0.58, rely=0.77)                                           
    
# get the choice of the user 
def get_scelta():                                       
    global lettera_in                                    
    lettera_in = lettera.get()                          
    lettera.delete(0,tk.END)                           
    if lettera_in!='l' and lettera_in!='w':
        domanda.config(text='thats not and option, do you want to guess the word or a letter? (w/l)')
        lettera.delete(0,tk.END)                       
        invio.config(command=get_scelta) 
    elif lettera_in == 'l':                                
        domanda.config(text='guess a letter')          
        invio.config(command=get_lettera)              
    else:                                               
        domanda.config(text='guess the word')           
        invio.config(command=get_parola)               

# checks if the letter the user gave is in the world 
def get_lettera():                                                                                                   
    global lettera_in, lives, word_state                                                                           
    lettera_in = lettera.get()                                                                                      
    if lettera_in in random_word:                                                                                  
        domanda.config(text='you guessed a letter, do you want to guess the word or a letter? (w/l)')               
        lettera.delete(0,tk.END)                                                                                   
        for i, letter in enumerate(random_word):                                                                    
            if letter == lettera_in:                                                                                
                word_state[i] = letter                                                                              
        parola.config(text=" ".join(word_state))                                                                   
        if ("".join(word_state))==random_word:                                                                     
            domanda.config(text='you guessed the word, congratulation')                                            
            parola.config(text=random_word)                                                                          
            bottone()                                                                                               
    else:
        lives -= 1                                                                                                  
        domanda.config(text='the letter is not in the word, do you want to guess the word or a letter? (w/l) ')    
        lettera.delete(0,tk.END)                                                                                    
        vite.config(text=f"{lives} lives left")                                                                   
    invio.config(command=get_scelta)                                                                                

# checks if the world the user gave is the same that was generated 
def get_parola():                                                          
    global lettera_in, lives,img                                           
    lettera_in = lettera.get()                                              
    if lettera_in == random_word:                                           
        domanda.config(text='you guessed the word, congratulation')         
        lettera.delete(0,tk.END)                                            
        parola.config(text=random_word)                                     
        bottone()                                                            
    else:
        lives = 0                                                           
        domanda.config(text='the word was not correct')                     
        lettera.delete(0,tk.END)                                            
        img = PhotoImage(file='fasi/i10.png')                               
        canvas.itemconfig(image_on_canvas,image=img)                         
    vite.config(text=f'{lives} lives left')                               

# creates the button to send the letter/world
invio = tk.Button(finestra, text='invio', command=get_scelta)               
invio.pack()                                                                
invio.place(relx=0.58, rely=0.807)                                         

# closes the window 
def i_am_become_death_the_destroyer_of_worlds():                            
    finestra.destroy()                                                      

# keep checking the number of lives the user has left 
def check():                                                                
    global img                                                               
    if lives == 0:                                                          
        domanda.config(text='the word was ' + ''.join(random_word))         
        img = PhotoImage(file='fasi/i10.png')                                
        canvas.itemconfig(image_on_canvas,image=img)                         
        finestra.after(6000,i_am_become_death_the_destroyer_of_worlds)      
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
            img = PhotoImage(file='fasi/i5.png')                            
        elif lives == 4:
            img = PhotoImage(file='fasi/i6.png')
        elif lives == 3:
            img = PhotoImage(file='fasi/i7.png')
        elif lives == 2:
            img = PhotoImage(file='fasi/i8.png')
        elif lives == 1:
            img = PhotoImage(file='fasi/i9.png')
        canvas.itemconfig(image_on_canvas,image=img)                       
        finestra.after(100,check)                                           


check()                     
finestra.mainloop()
