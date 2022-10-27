from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import colorgram as cg
import pandas as pd
import os
import random
import string
import pyperclip

# ------------------------ CONSTANTS -------------------------
IMAGE_PATH = 'lock-1.png'
FONT = ("Courier", 16, "bold")
VAULT_PATH = 'vault.txt'
PWD_LENGHT = 12


# ------------------ FILE READ/WRITE OPERATIONS ----------------------

def save_pwd():
    website_data = website_field.get()
    login_data = login_field.get()
    pwd_data = pwd_field.get()
    # print(website_data, login_data, pwd_data)

    if website_data == '' or pwd_data == '':
        messagebox.showwarning(title="Oops", message="Required fields are empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are details entered:\n"
                                               f"Email: {login_data}\n"
                                               f"Password: {pwd_data}\n"
                                                   f"Is it Ok to save?")
        if is_ok:
            data = pd.DataFrame({'website': [website_data],
                                 'login': [login_data],
                                 'password': [pwd_data]})
            data.to_csv(VAULT_PATH, mode='a', header=not os.path.exists(VAULT_PATH), index='')
            clear_fields()

def search_website():
    try:
        website_data = website_field.get()
    finally:
        if website_data == '':
            messagebox.showinfo(title="Website", message="The website field is empty!")
    try:
        data = pd.read_csv(VAULT_PATH)
        website_row = data[data.website == website_data]
        messagebox.showinfo(title="Credentials", message=f"Email: {website_row.login[0]},\n"
                                                     f"Password: {website_row.password[0]}")
    except FileNotFoundError:
        messagebox.showinfo(title="Vault", message="The vault not found...")
    except Exception as e:
        print(e)




def clear_fields():
    website_field.delete(0, END)
    login_field.delete(0, END)
    pwd_field.delete(0, END)

# ------------------ GENERATE PASSWORD ----------------------

def pwd_generate():
    password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(PWD_LENGHT)])
    pwd_field.delete(0, END)
    pwd_field.insert(END, password)
    # Save variable to clipboard
    pyperclip.copy(password)


# ------------------------ UI SETUP --------------------------
window = Tk()
window.title("Password manager")
window.geometry("500x300")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=128, height=128)
canvas.grid(row=1, column=2)

# Load the image
img=ImageTk.PhotoImage(file=IMAGE_PATH)

# Add the image in the canvas
canvas.create_image(64, 64, image=img, anchor="center")


# Buttons
search_button = Button(text='Search', width=13, command=search_website)
search_button.grid(row=2, column=3)

add_button = Button(text='Add', width=25, command=save_pwd)
add_button.grid(row=5, column=2, columnspan=2)

gen_pwd_button = Button(text='Generate password', command=pwd_generate)
gen_pwd_button.grid(row=4, column=3)


# Labels
website_text = Label(text="Website:", font=FONT)
website_text.grid(row=2, column=1)

login_text = Label(text="Emain/Username:", font=FONT)
login_text.grid(row=3, column=1)

pwd_text = Label(text="Password:", font=FONT)
pwd_text.grid(row=4, column=1)


# Input
website_field = Entry(width=13)
website_field.grid(row=2, column=2)

login_field = Entry(width=30)
login_field.grid(row=3, column=2, columnspan=2)

pwd_field = Entry(width=13)
pwd_field.grid(row=4, column=2)
# # ------------------------ Extract colors from Image ------------------------
# def _from_rgb(rgb):
#     """translates an rgb tuple of int to a tkinter friendly color code
#     """
#     r, g, b = rgb
#     return f'#{r:02x}{g:02x}{b:02x}'
#
# def getColor(imagePath):
#     color_list = cg.extract(imagePath, 2 ** 32)
#     color_palette = []
#
#     for count in range(len(color_list)):
#         rgb = color_list[count]
#         color = rgb.rgb
#         color = [color.r, color.g, color.b]
#         color_palette.append(color)
#     return color_palette
#
# colors = getColor(IMAGE_PATH)

# for color in colors:
#     print(color)
#     # window.after(3000, window.config(bg=_from_rgb(color)))






window.mainloop()

