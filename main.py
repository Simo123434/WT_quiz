'''
Quiz application for Warthunder tanks
GUI using tkinter
'''
from tkinter import *
from PIL import ImageTk,Image
import os
import random


# Quiz interface class
class Quiz:
    def __init__(self):
        # intialize the window
        self.window = Tk()
        # Set title
        self.window.title("Warthunder Quiz")
        # set window size
        self.window.geometry("1000x800")
        
        # load warthunder logo image
        self.img = ImageTk.PhotoImage(Image.open("./Images/War-Thunder-logo.jpg"))
        # create canvas
        self.canvas = Canvas(self.window, width=1000, height=800)
        self.canvas.pack()
        # load image on canvas
        self.canvas.create_image(500, 400, anchor = S ,image=self.img)
        # Create label
        self.welcome_label = self.canvas.create_text(500, 500, text="Welcome to the Warthunder Quiz", font=("Arial", 30))
        
        # create Begin Button under welcome_label
        self.begin_button = Button(self.window, text="Begin", height=5, width=30, command=self.select_country)
        self.begin_button.place(x=400, y=550)
        self.window.mainloop()

    def select_country(self):
        # clear screen and show country selection
        self.window.destroy()
        self.window = Tk()
        self.window.title("Warthunder Quiz")
        self.window.geometry("1000x800")
        # create heading
        self.canvas = Canvas(self.window, width=1000, height=800)
        self.canvas.pack()
        self.canvas.create_text(500, 100, text="Select your country", font=("Arial", 30))
        
        # germany button
        self.germany = Button(self.window, text="Germany", height=5, width=25, command=self.germany)
        self.germany.place(x=100, y=200)
        # usa button
        self.usa = Button(self.window, text="USA", height=5, width=25)
        self.usa.place(x=300, y=200)
        # ussr button
        self.ussr = Button(self.window, text="USSR", height=5, width=25)
        self.ussr.place(x=500, y=200)
        # uk button
        self.uk = Button(self.window, text="UK", height=5, width=25)
        self.uk.place(x=700, y=200)
        # japan button
        self.japan = Button(self.window, text="Japan", height=5, width=25)
        self.japan.place(x=100, y=300)
        # china button
        self.china = Button(self.window, text="China", height=5, width=25)
        self.china.place(x=300, y=300)
        # italy button
        self.italy = Button(self.window, text="Italy", height=5, width=25)
        self.italy.place(x=500, y=300)
        # france button
        self.france = Button(self.window, text="France", height=5, width=25)
        self.france.place(x=700, y=300)
        # sweden button
        self.sweden = Button(self.window, text="Sweden", height=5, width=25)
        self.sweden.place(x=100, y=400)
        # israel button
        self.israel = Button(self.window, text="Israel", height=5, width=25)
        self.israel.place(x=300, y=400)
    
    def germany(self):
        self.window.destroy()
        self.window = Tk()
        self.window.title("Warthunder Quiz")
        self.window.geometry("1000x800")
        # create heading
        self.canvas = Canvas(self.window, width=1000, height=800)
        # Text at top
        self.canvas.create_text(500, 100, text="What is this tank?", font=("Arial", 30))
        self.canvas.pack()
        images = []
        answers = ["panzer 3 e", "panzer 3 f", "panzer 2 c"]
        for file in os.listdir("./Images/Germany"):
            if file.endswith(".jpg"):
                images.append(file)
               
        for i in images:
            # pick a random image and show on screen
            self.img = ImageTk.PhotoImage(Image.open("./Images/Germany/" + random.choice(images)))
            self.canvas.create_image(500, 600, anchor = S ,image=self.img)
            #create entry box to get input
            self.entry = Entry(self.window, width=30)
            self.entry.place(x=400, y=600)
            # create submit button
            self.submit = Button(self.window, text="Submit", height=2, width=25)
            self.submit.place(x=400, y=620)
            answer = answers[images.index(i)]
            # check if answer is correct
            
            
        
    
    
        


quiz = Quiz()






