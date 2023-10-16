from tkinter import *
from tkinter import messagebox
import pyperclip
import json

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pw():
    password_entry.delete(0, END)

    password_list =  [random.choice(letters) for char in range( random.randint(8, 10)) ]
    password_list += [random.choice(symbols) for char in range( random.randint(2, 4)) ]
    password_list += [random.choice(numbers) for char in range( random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def add_press():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password": password,
        }
    }
    if (len(website) == 0 or len(password) == 0):
        messagebox.showerror(message="You left some fields empty lad")
        return
    try:
        if(messagebox.askokcancel(title= website,message=f" These are the details entered \n email:{email}\n password:{password}\n is it ok to save?")):

            with open("data.json","r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)

    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_json():
    website = website_entry.get()
    try:
        with open("data.json","r")as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Error ",message="There is no file with that name")
    else:
        try:
            messagebox.showinfo(title=website,message= f"Email : {data[website]["email"]}\n Password:{data[website]["password"]} ")
        except KeyError:
            messagebox.showinfo(title="Key Error", message=f"You have no passwords for {website}")


window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)
canvas = Canvas(height =200 ,width =200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row = 0 ,column=1)
website_text = Label(text="Website:")
website_text.grid(row=1,column=0)
email_text = Label(text="Email/Username:")
email_text.grid(row=2,column=0)
password_text = Label(text="Password:")
password_text.grid(row=3,column=0)
website_entry = Entry(width= 35)
website_entry.grid(row=1,column=1)
website_entry.focus()
website_button = Button(text="Search",width=15,command = search_json)
website_button.grid(row =1 , column = 2)
email_entry = Entry(width=53)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xristakos167@hotmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)
password_button = Button(text="Generate Password",command=generate_pw)
password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=45,command=add_press)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
