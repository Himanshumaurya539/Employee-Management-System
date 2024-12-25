#importing all classes and methods inside customtkinter
from customtkinter import *
from PIL import Image # importing pillow library to imprort images 
from tkinter import messagebox
def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror('Error','All fields are required')

    elif usernameEntry.get()=="himanshu" or passwordEntry.get()=="1234":
        messagebox.showinfo('success','login successful')

    else:
        messagebox.showerror('Error','Wrong credentials')
        root.destroy()  #This will destroy the window 
        import ems

#creating window
root =CTk()

root.geometry('930x478')  #To set height and width of window

root.resizable(0,0) #To have fix size of the window and maximum button will be disabbled
root.title('login page') #To have a title of the CTK page
#creating and importing the image 
image = CTkImage(Image.open('login_img.png'),size=(930,478)) 
#labelling the created image 
imageLabel = CTkLabel(root,image=image,text='') #Empty text here will remmove default text from image 
imageLabel.place(x=0,y=0) #placing the image 

#Creating the heading text 
headinglabel = CTkLabel(root,text='Employee management System',bg_color='#031434',font=('Goudy old Style',30,'bold'))
headinglabel.place(x=280,y=200) #placing the heading text 

usernameEntry= CTkEntry(root,placeholder_text='Enter user name')
usernameEntry.place(x=400,y=250)

passwordEntry= CTkEntry(root,placeholder_text='Enter password',show='*')
passwordEntry.place(x=400,y=280)

loginButton = CTkButton(root,text='login',command=login)
loginButton.place(x=400,y=310)
root.mainloop()  #this keep the window on hold 