from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passw_letters = [choice(letters) for char in range(randint(8, 10))]
    passw_symbols = [choice(symbols) for char in range(randint(2, 4))]
    passw_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = passw_letters + passw_symbols + passw_numbers

    shuffle(password_list)

    password = "".join(password_list)
    passw_input.delete(0, 'end')
    passw_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = email_input.get()
    password = passw_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"Website: {website}", message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \n Is this ok?")
    if is_ok:
        try:
            with open("info.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except json.decoder.JSONDecodeError:
            with open("info.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("info.json", "w") as data_file:
                # Updating old data with new data
                data.update(new_data)
                #Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, 'end')
            passw_input.delete(0, 'end')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    website = web_input.get()

    try:
        with open("info.json", "r") as data_file:
            data = json.load(data_file)

    except json.decoder.JSONDecodeError:
        not_file = messagebox.showwarning(title=f"Website: {website}", message="No Data File Found")
        print(not_file)

    else:
        if website in data:
            email = data[website]['email']
            passw = data[website]['password']

            messagebox.showinfo(title=f"Website: {website}", message=f"Email: {email} \nPassword: {passw}")
            web_input.delete(0, 'end')
        else:
            messagebox.showinfo(title=f"Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

#Img
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

#Website
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

#Entry Website
web_input = Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()

#Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

#Entry Email/Username
email_input = Entry(width=52)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, "amdituris@hotmail.com")

#Password
passw = Label(text="Password:")
passw.grid(column=0, row=3)

#Entry Password
passw_input = Entry(width=33)
passw_input.grid(column=1, row=3)

#Search Button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

#Password Button
passw_button = Button(text="Generate Password", width=15, command=random_password)
passw_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
