import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font


class build:
    def tex_update(word,name):
        name = tk.Label(text=word)
    def createLabel1(menu, word, xpos, ypos, fontsize):
        tk.Label(menu, text=word, font=("Times", fontsize, "bold italic")).place(x=xpos, y=ypos)
    def createLabel(menu, word, xpos, ypos, fontsize):
        label = tk.Label(menu, text=word, font=("Times", fontsize, "bold italic")).place(x=xpos, y=ypos)

    def createBtn(menu, word, xpos, ypos, width, height, btn, fontsize, add_img):
        if add_img == "no":
            img = None
        else:
            image = Image.open(add_img)
            image = image.resize((width, height))
            img = ImageTk.PhotoImage(image)
        btn = tk.Button(menu, command=btn,image=img, text=word, font=("Times", fontsize, "bold italic"), compound="center", bd=1, height=height, width=width)
        #   bd='70' can also be used in tk.button might use later
        btn.place(x=xpos, y=ypos)
        btn.image = img
    def create_img(win, xpos, ypos, width ,height, img):
        path = Image.open(img)
        image = path.resize((width,height))
        render = ImageTk.PhotoImage(image)
        label = tk.Label(win, image=render, font=100, compound="center")
        label.place(x=xpos, y=ypos)
        label.image = render

    def create_icon(menu, icon):
        ico = Image.open(icon)
        photo = ImageTk.PhotoImage(ico)
        menu.wm_iconphoto(False, photo)

    def create_window(win,size, name):
        if win == "buy":
            new_win = tk.Tk()
            new_win.geometry(size)
            new_win.title(name)
            new_win.config(bg="light blue")

        else:
            win.geometry(size)
            win.title(name)
            win.config(bg="light blue")




