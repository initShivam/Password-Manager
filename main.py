from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            '0','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    

    password = ""

    password_letters = [choice(letters) for _ in range(randint(2, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 2))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the password to clipboard
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # website = website_entry.get()
    # email = email_entry.get()
    # password = password_entry.get()

    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    #     if is_ok:
    #         with open(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\password-manager-start\Datas.txt", "a") as data_file:
    #             data_file.write(f"{website} | {email} | {password}\n")
    #             website_entry.delete(0, END)
    #             password_entry.delete(0, END)
    from tkinter import messagebox

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Missing Information",
            message="Please fill in both the Website and Password fields."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=f"Confirm Details for {website}",
            message=f"Email: {email}\nPassword: {password}\n\nDo you want to save these details?"
        )
        if is_ok:
            try:
                with open(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\password-manager-start\Datas.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data:\n{e}")
            else:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo("Success", "Credentials saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)
window.config(width=400, height=400)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_1 = Label(text="Website:")
label_1.grid(row=1, column=0, sticky="S")
label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0, sticky="S")
label_3 = Label(text="Password:")
label_3.grid(row=3, column=0, sticky="S")

# Entries
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1, sticky="E",)

# generate_password_button.grid(row=3, column=2, sticky="W",padx=10, pady=20)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="s",)

window.mainloop()
