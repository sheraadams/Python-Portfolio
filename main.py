from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

back = "#278ED5"
fore = "#65FC6A"

window = tk.Tk()
window.geometry('900x970')

top= tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

def equations(panel):
    path = '2.jpeg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "Derivative Properties:\nSum and difference rules: (f+-g)' = f'+-g'\n"
                               "Power rule: x^n is nx^n-1, we apply this to \n"
                                "The derivative of any constant (c) * x is c\n"
                                "The derivative of a constant is zero\n\n"
                                "Derivative Equations:"
                                "\nThe product rule: (u*v)'= u'v+uv'\nThe quotient rule: (f/g)'= gf'=fg'/g^2 \n"
                                "The chain rule: f(g(x))'= f'(g(x))g'(x)\n\n"
                                "Antiderivative:\nThe antiderivative of x^n(dx)= (1/(n+1))(x)^(n+1)+C\n\n"
                                "Linear Equations:\n"
                                "The equation for a line is y= mx+b \nThe equation for a point on a line y1-y2= m(x1-x2)\n\n"
                                "Linear Approximation:\n"
                                "Linear approximation formula: L(x)= f(a)+f'(a)(x-a)\n\n"
                                "Mean Value Theorem:\n Mean Value Theorem formula: f'c = f(b)-f(a)/b-a\n\n\n\n\n\n\n" )
         # this creates a new label to the GUI
    label.pack()


def sketching(panel):
    path = '3.jpeg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nSketching:\n"
                  "First Derivative:\nWe use the first derivative of f(x) to find the critical points and intervals "
                  "of increase and decrease.\n\n"
                  "Critical Points:\nWe find critical points by setting the derivative to 0. To find exact"
                  " points, plug the x value into \n\toriginal equation\n\n"
                  "Intervals:\nTo find intervals of increase or decrease, we select arbitrary intervals and plug "
                  "then into derivative to find \n\tthe sign (positive or negative).\n\n"
                  "Second Derivative:\nWe use the second derivative of f(x) to find the points of inflection and intervals of concavity\n\n"
                  "Concavity: We find concavity intervals by selecting arbitrary intervals and plugging them into the second derivative "
                  "\nto find the sign (positive or negative).\n\n"
                  "Inflection Points:\nWe find the inflection points by setting the second derivative"
                  "ve to zero. To find exact points of \n\tinflection, we plug the x values into the original equation\n\n"
                  "Horizontal Asymptotes:\n"
                  "If degree numerator = denominator HA = degree of the powers\n"
                  "if degree numerator < denominator HA = 0\n"
                  "if degree numerator > denominator no HA\n\n"
                  "Vertical Asymptotes:\n"
                  "Set denominator = 0, if there is no denominator, there is no HA\n\n")
    label.pack()


def trigonometry(panel):
    path = '4.jpeg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text="Trigonometric Derivatives \nd/dx sin(x) = cos(x) \nd/dx cos(x)=−sin(x)\nd/dx tan(x)=sec2(x)\n"
          "d/dx sec(x)=sec(x)tan(x)\nd/dx cot(x)=−csc2(x)\nd/dx csc(x)=−csc(x)cot(x)\n\n"
          "Trigonometric Ratios\nSin θ = Opposite side/Hypotenuse\nCos θ = Adjacent Side/Hypotenuse\n"
          "Tan θ = Opposite side/Adjacent Side\nSec θ = 1/cos θ = Hypotenuse/Adjacent Side\n"
          "Csc θ = 1/Sin θ = Hypotenuse/Opposite side\nCot θ = 1/tan θ = Adjacent Side/Opposite side\n\n"
          "Trigonometric Identities\nSin θ = 1/Csc θ or Csc θ = 1/Sin θ\nCos θ = 1/Sec θ or Sec θ = 1/Cos θ\n"
          "Tan θ = 1/Cot θ or Cot θ = 1/Tan θ\n"
          "Tan θ = Sin θ/Cos θ\nCot θ = Cos θ/Sin θ\n\n"
          "Pythagorean Identities\nsin2 a + cos2 a = 1\n1+tan2 a  = sec2 a\ncsc2 a = 1 + cot2 a\n\n\n")
    label.pack()
def physics(panel):
    path = '5.jpeg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "Area formulas:\n"
          "Circle = pi*r^2 with Derivative: DA/Dt = 2pi*r(dr/dt)\n"
          "Sphere = 4pi*r^2 with Derivative: DA/Dt = 8pi*r\n"
          "Triangle = (b*h)/2\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    label.pack()


path = '1.jpeg'
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, fg= back, image = img)
panel.image = img
panel.pack(side = "top", fill = "both", expand = "yes")
label = Label(window, fg= back, text="", anchor= "n")


next_button = tk.Button(window, bg = "white", fg= back, text = "Equations",command = lambda: equations(panel))
next_button.pack(in_= bottom, side="left")
prev_button = tk.Button(window, bg = "white", fg= back, text = "Sketching",command = lambda: sketching(panel))
prev_button.pack(in_= bottom, side="right")
next_button = tk.Button(window, bg = "white", fg= back, text = "Trigonometry",command = lambda: trigonometry(panel))
next_button.pack(in_= bottom, side="left")
prev_button = tk.Button(window, bg = "white", fg= back, text = "Physics",command = lambda: physics(panel))
prev_button.pack(in_= bottom, side="right")


window.mainloop()