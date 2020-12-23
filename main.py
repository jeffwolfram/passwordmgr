from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pandas


COLOR = "#ddd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)

def find_password():
    list = pandas.read_json('password.json')
    print(list)
    messagebox.showinfo(title="Password Search", message=f"Website: \nPassword: ")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    password = password_input.get()
    email = email_input.get()
    new_data = {
        website: {
            "email": email,
                "password": password
        }
    }
    if password == '' or website == '':
        messagebox.showinfo(title='Missing', message="Please don't leave any fields open!")
    else:
        try:
            with open("password.json", 'r') as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password.json", 'w') as data_file:
                # saving new data if file did not exist
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data
            data.update(new_data)

            with open("password.json", 'w') as data_file:

                #saving old data
                json.dump(data, data_file, indent=4)
                print(password)
                website_input.delete(0, END)
                password_input.delete(0, END)



# ---------------------------- UI SETUP -------------------------------



window = Tk()
window.title("Passwoed Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 20))
website_label.grid(row=1, column=0)

website_input = Entry( width=21 )
website_input.grid(row=1, column=1, columnspan=1)
website = website_input.get()

website_button = Button(text="Search", highlightbackground=COLOR, width=11, command=find_password)
website_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", font=("Arial", 20))
email_label.grid(row=2, column=0)


email_input = Entry(width=35 )
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "jeffwolfram@gmail.com")


password_label = Label(text="Password:", font=("Arial", 20))
password_label.grid(row=3, column=0)


password_input = Entry( width=21, textvariable="StringVar")
password_input.grid(row=3, column=1)


generate_password_button = Button(text="Generate Password", command=generate_password, highlightbackground=COLOR)
generate_password_button.grid(row=3, column=2)


add_button = Button( text="Add", width=36, highlightbackground=COLOR, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()