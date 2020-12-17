from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP -------------------------------



window = Tk()
window.title("Passwoed Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 20))
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:", font=("Arial", 20))
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 20))
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add")



window.mainloop()