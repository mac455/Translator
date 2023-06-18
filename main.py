#First, create virtual enviromenent and install tkinter and translate package. 
from tkinter import *
from translate import Translator

# Initialize GUI window

screen = Tk()
screen.title('Translator GUI by Mac')
# Stringvar holds a string value - in this case the language input by user or the translated output 
input = StringVar()
output = StringVar()
Languages = {'Hindi', 'German', 'English', 'French', 'Spanish'}

# .set method sets the value of the variable - sets to English but can be changed later to account for user input
input.set('English')
output.set('German')
# Translate function
def Translate():
    translator = Translator(from_lang= input.get(),to_lang=output.get()) 
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

# Choosing input language
InputLanguageChoiceMenu = OptionMenu(screen,input,*Languages)
Label(screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)

# Choosing output language 
NewLanguageChoiceMenu = OptionMenu(screen,output,*Languages)
Label(screen,text="Translation").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

# Adding text to display on input box                       
Label(screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(screen,textvariable=TextVar).grid(row=2,column = 1)

# Adding text to display on output box
Label(screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(screen,textvariable=OutputVar).grid(row=2,column = 3)

#Translate button
B = Button(screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
 
mainloop()
