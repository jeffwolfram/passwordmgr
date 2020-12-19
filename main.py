from tkinter import *
COLOR = "#ddd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("password.txt", 'a+') as file1:
        file1.write(f'{website} | {email} | {password}')
        print(password)
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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website = website_input.get()

email_label = Label(text="Email/Username:", font=("Arial", 20))
email_label.grid(row=2, column=0)


email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "jeffwolfram@gmail.com")
email = email_input.get()

password_label = Label(text="Password:", font=("Arial", 20))
password_label.grid(row=3, column=0)


password_input = Entry(width=21)
password_input.grid(row=3, column=1)
password = password_input.get()

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightbackground=COLOR, command=save())
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()