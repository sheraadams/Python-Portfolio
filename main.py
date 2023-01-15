from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

back = "black"
fore = "#65FC6A"
window = tk.Tk()
window.configure(bg="white")
window.title("Shera Adams Portfolio")
window.geometry('1300x800')
top= tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

def Wormhole(panel):
    path = 'wormhole.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()

def Pong(panel):
    path = 'pong.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()


def Breakout(panel):
    path = 'Breakout.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()

def Pokemon(panel):
    path = 'pokemon.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()

def PVP(panel):
    path = 'pvp.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()


def Shapes(panel):
    path = 'shapes.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()


def Shading(panel):
    path = 'shading.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()


def Textures(panel):
    path = 'textures.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()

def Scenes(panel):
    path = 'scene.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "")
    label.pack()




path = '3.png'
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window,bg= "white", fg= "white", image = img, borderwidth=0, highlightthickness=0)
panel.image = img
panel.pack()
path = 'wormhole.png'
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, bg= "white", fg= "white", image = img)
panel.image = img
panel.pack(side = "top", fill = "both", expand = "yes")
label = Label(window, fg= "black", text="Portfolio", anchor= "n")

button1 = tk.Button(window, bg = "white", fg= back, text = "Wormhole",command = lambda: Wormhole(panel))
button1.pack(in_= bottom, side="left")
button2 = tk.Button(window, bg = "white", fg= back, text = "Pong",command = lambda: Pong(panel))
button2.pack(in_= bottom, side="left")
button3 = tk.Button(window, bg = "white", fg= back, text = "Breakout",command = lambda: Breakout(panel))
button3.pack(in_= bottom, side="left")
button4 = tk.Button(window, bg = "white", fg= back, text = "Pokemon",command = lambda: Pokemon(panel))
button4.pack(in_= bottom, side="left")
button5 = tk.Button(window, bg = "white", fg= back, text = "PVP",command = lambda: PVP(panel))
button5.pack(in_= bottom, side="left")
button6 = tk.Button(window, bg = "white", fg= back, text = "Shapes",command = lambda: Shapes(panel))
button6.pack(in_= bottom, side="left")
button7 = tk.Button(window, bg = "white", fg= back, text = "Shading",command = lambda: Shading(panel))
button7.pack(in_= bottom, side="left")
button8 = tk.Button(window, bg = "white", fg= back, text = "Textures",command = lambda: Textures(panel))
button8.pack(in_= bottom, side="left")
button9 = tk.Button(window, bg = "white", fg= back, text = "Scenes",command = lambda: Scenes(panel))
button9.pack(in_= bottom, side="left")

window.mainloop()
