# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:29:41 2024

@author: Dell
"""

from tkinter import * 
import wikipedia

#Fetching the data
def get_data():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        #Fetch the summary for the provided entry value
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        #Handle any exceptions (invalid input or poor internet connection)
        answer.insert(INSERT, "ERROR! Invalid input or poor internet connection")

#setting the language for Wikipedia to English
wikipedia.set_lang("en")

#create the main application window
adw= Tk()
adw.title("Wikipedia Search") #Set the title of the window

#create a topframe to hold the search button and entry values
topframe = Frame(adw)
entry = Entry(topframe)
entry.grid(row=0, column=0, padx=5, pady=5) 


#create a search button that calls the get_data function when clicked

button = Button(topframe, text="search",activeforeground="white", activebackground="grey", command=get_data)
button.grid(row=0, column=1, padx=5, pady=5)

topframe.pack(side = TOP)

#create a bottom frame to hold the text box for displaying results and also for scrolling 

bottomframe = Frame(adw)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

#create a answer textbox to display the search results with a specific height and width 
answer =  Text(bottomframe, width=65, height=30, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

#start the tkinter loop

adw.mainloop()