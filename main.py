from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    p_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    for char in range(1, random.randrange(4,10) + 1):
        password_list.append(random.choice(letters))

    for char in range(1, random.randrange(1,3) + 1):
      password_list += random.choice(symbols)

    for char in range(1, random.randrange(1,3) + 1):
      password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = ""
    for char in password_list:
        password += char
    p_entry.insert(0, f'{password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if w_entry.get() == '' or p_entry.get() == '':
        messagebox.showwarning(title="Warning",message="Please don't leave any fields empty.")

    else:
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(f"{p_entry.get()}")
        is_ok = messagebox.askokcancel(title=w_entry.get(),
                                       message=f"Details entered: \nEmail:{e_entry.get()}\nPassword:{p_entry.get()}\nIs this correct?")
        if is_ok:
            with open("Password.txt", "a") as file:
                file.write(f" {w_entry.get()} | {e_entry.get()} | {p_entry.get()}\n")
                w_entry.delete(0,'end')
                p_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20, bg='white')


# Logo
canvas = Canvas(width=200, height=200,bg='white', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

website = Label(text="Website:",fg='black',bg='white', font=('Arial',10,"bold"))
website.grid(column=0, row=1)
w_entry = Entry(width=35)
w_entry.grid(row=1, column=1, columnspan=2,sticky=W)
web = w_entry.get()

email = Label(text="Email/Username:",fg='black',bg='white', font=('Arial',10,"bold"))
email.grid(column=0, row=2)
e_entry = Entry(width=35)
e_entry.insert(0,"Gassergaballa@gmail.com")
e_entry.grid(row=2, column=1, columnspan=2,sticky=W)

password = Label(text="Password:",fg='black',bg='white', font=('Arial',10,"bold"))
password.grid(column=0,row=3)
p_entry = Entry(width=35)
p_entry.grid(row=3, column=1, columnspan=2,sticky=W)
print(p_entry.get())

add = Button(text="Add",width=35, command = save)
add.grid(column=1,row=4,sticky=W)

generate = Button(text="Generate Password",width=15,command=password_generate)
generate.grid(column=2,row=3,columnspan=2,sticky=W)




window.mainloop()
