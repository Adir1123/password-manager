from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END,password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_input.get()
    password_manager = password_input.get()

    new_data = {

       website: {
            "email" : email,
            "password" : password_manager,
       }
    }


    if len(website) == 0 and len(password_manager) == 0:
        messagebox.showinfo(title="Ops",message="No Website and Password entered")
    elif len(password_manager) == 0:
        messagebox.showinfo(title="Ops",message="No Password entered")
    elif len(website) == 0:
        messagebox.showinfo(title="Ops",message="No Website entered")
    else:
        with open("data.json", "w") as data_file:  ##creating data.txt file with append mode to add my passwords
            json.dump(new_data, data_file,indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


window = Tk()
window.title("My password manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0,sticky="w")
user_name = Label(text="User Name:")
user_name.grid(row=2,column=0,sticky="w")
password_label = Label(text="Password:")
password_label.grid(row=3,column=0,sticky="w")


#Entries 
website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2,sticky="ew")

email_input = Entry(width=35)
email_input.insert(END,"adirgabay9@gmail.com")
email_input.grid(row=2,column=1,columnspan=2,sticky="ew")


password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

# Buttons
generate_password = Button(text="Generate Password",command=password_generate)
generate_password.grid(row=3, column=2,padx=0, sticky="w")

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky="ew")

window.mainloop()