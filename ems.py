from customtkinter import *
from PIL import Image
from tkinter import ttk , messagebox #this package is the extention of tkinter model 
import database 

#functions 

def treeview_data():
    global tree
    employees=database.fetch_employees()
    for employee in employees:
        tree.insert('','end',values=employee) 



def add_employee():
   if idEntry.get() =="" or phoneEntry.get() =="" or nameEntry.get()=="" or salaryEntry.get()=="" :
        messagebox.showerror('Error','All fields are required')
        #messagebox takes two argument i.e title and messgae to display 

   elif database.id_exists(idEntry.get()): 
       messagebox.showerror('Error','Id already exists') 

   else:
       database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())

       messagebox.showinfo('SUCCESS','Data is Added')
#GUI part 
window =CTk()
window.geometry('930x580+100+100')
#  +100+100 means adjusting window from both axes to keep fix 
window.resizable(0,0)
window.title('Employee Management System')
logo= CTkImage(Image.open('image.png'),size=(930,200))
logolabel = CTkLabel(window,image=logo,text='')
#grid devide the windows into rows and columns 
logolabel.grid(row=0,column=0,columnspan=2)

#Creating left frame window 
leftFrame = CTkFrame(window) #we can use fg_color = "#43548" to change the color of left window 
leftFrame.grid(row=1,column = 0) 

#Creating label for id 
idLabel= CTkLabel(leftFrame,text='Id :',font=('arial',18,'bold'))
#padx=(0,20) will create a space for ID : 
#0 perform padding in left side where as 20 on right side 
idLabel.grid(row=0,column=0,padx=20,pady=10)
#creating a entry box usiing ctkEntry()
idEntry = CTkEntry(leftFrame,font=('ariel',15,'bold'),width=200)
idEntry.grid(row=0,column=1) #It will create entry field at column 1 

#For name 
nameLabel= CTkLabel(leftFrame,text='Name :',font=('arial',18,'bold')) # we can also add text_color= "#45845"
nameLabel.grid(row=1,column=0,padx=20,pady=10)
nameEntry = CTkEntry(leftFrame,font=('ariel',15,'bold'),width=200)
nameEntry.grid(row=1,column=1) #It will create entry field at column 1

#Phone label 
phoneLabel= CTkLabel(leftFrame,text='Phone No.:',font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=20,pady=15)
phoneEntry =CTkEntry(leftFrame,font=('ariel',15,'bold'),width=200)
phoneEntry.grid(row=2,column=1) #It will create entry field at column 1

#For role 
roleLabel= CTkLabel(leftFrame,text='Role :',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15)
#Creating a options for selecting 
role_options=['Web Developer','Data scientist','Cloud Architect','Network Engineer',
              'Devop Engineer','It Consultant']
roleBox= CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0]) #To show first value from box list 
#for gender 
genderLabel= CTkLabel(leftFrame,text='Gender :',font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15)
gender_option =['Male','Female','Other']
genderBox= CTkComboBox(leftFrame,values=gender_option,width=180,font=('arial',15,'bold'),state='readonly')
#state = 'readonly' will show empty box 
genderBox.grid(row=4,column=1)

#for salary 
salaryLabel= CTkLabel(leftFrame,text='Salary :',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15)
salaryEntry =CTkEntry(leftFrame,font=('ariel',15,'bold'),width=200)
salaryEntry.grid(row=5,column=1) #It will create entry field at column 1


#Creating right frame window
rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_option = ['Id','Name','Phone','Role','Gender','Salary']
searchBox= CTkComboBox(rightFrame,values=search_option,width=180,font=('arial',15,'bold'),state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry =CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightFrame,text='search',width=100)
searchButton.grid(row=0,column=2)

showallButton = CTkButton(rightFrame,text='Show all ',width=100)
showallButton.grid(row=0,column=3,pady=5)

#Creating tree view 
tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan =4 )
#columnspan devides thr column in 4 parts 

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
#this will only create columns in tree
#Labbeling heading below
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')#this will only show headings mentioned in columns no extra columns

tree.column('Id',width=90)
tree.column('Name',width=180)
tree.column('Phone',width=100)
tree.column('Role',width=120)
tree.column('Gender',width=80)
tree.column('Salary',width=150)
# this will change the heading in tree 
style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',12,'bold'))
scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL)
# to stick scrollbar totally on north south direction use sticky = 'ns'
scrollbar.grid(row=1,column=4,sticky='ns')

#adding new buttons frame to add multiple buttons below the LHS &RHS frame
buttonFrame = CTkFrame(window)
buttonFrame.grid(row=2,column=0,columnspan=2)

newbutton = CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
#corner_radius is to fix corners 
newbutton.grid(row=0,column=0,pady=5)

addbutton = CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15, command = add_employee)
#command name written is nothing but function name mentioned above
addbutton.grid(row=0,column=1,padx=5)
# padx is padding in x axis and pady is padding in y axis 

updatebutton = CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
updatebutton.grid(row=0,column=2,padx=5)

deletebutton = CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deletebutton.grid(row=0,column=3,padx=5)

deleteallbutton = CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteallbutton.grid(row=0,column=4,padx=5)


window.mainloop()
