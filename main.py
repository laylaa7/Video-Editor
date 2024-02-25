from tkinter import *
from PIL import Image , ImageTk

# widgets = GUI elements like btns , textboxes , labels , images 
# windows = serves as a container to hold widgets

window = Tk() #instantiate an instance of a window
window.geometry("450x450")
window.title("video editing interface by layla")
image= Image.open("images/redrum.jpeg")
icon = ImageTk.PhotoImage(image)

#window.config(background="#4e42f5"),
#label = Label(window,text="hello world",font=('Arial',40,'bold') ,fg='#4e42f5' ,bg="black" ,image=icon  compound='bottom')
#label.place(x=1,y=0)
#label.pack()
label1 = Label(window,text="Input video File:").grid(row=0,column=0)
label2 = Label(window,text="Output Folder :").grid(row=1,column=0) 
label3= Label(window,text="Intro Video File (Optional) :").grid(row=2,column=0)
label4 = Label(window,text="Time Points :").grid(row=3,column=0)

Buttonexplore = Button(window,text="browse",command=BROWSE).grid(row=0,column=1)
def click():
    print("hello layla")
button = Button(window,text="click me")
button.config(command=click)
button.config(font=("Ink Free",50,"bold"))
#button.pack()


window.mainloop() # place el window on screen and listen for events
