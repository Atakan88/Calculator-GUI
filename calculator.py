import math
from tkinter import *
from math import *

# borderwidth = bd
window = Tk()
window.title("Calculator")
window.geometry("355x450")
window.configure(bg="#737373")
window.resizable(width=False, height=False)
button_frame = Frame(window, bg="#737373")
button_frame.pack()
equation = StringVar()
equation.set(0)
expression_field = Entry(
    button_frame,
    textvariable=equation,
    justify="right",
    font=("arial", 20, "bold"),
)

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("0")


def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def sinus(num):
    pass


def cosinus():
    pass


def log():
    pass


buttonsin = Button(
    button_frame,
    text="sin",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    state="disabled",
)
buttoncos = Button(
    button_frame,
    text="cos",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    state="disabled",
)
buttonlog = Button(
    button_frame,
    text="log10",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    state="disabled",
)
button1 = Button(
    button_frame,
    text="1",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((1)),
)
button2 = Button(
    button_frame,
    text="2",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((2)),
)
button3 = Button(
    button_frame,
    text="3",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((3)),
)
add = Button(
    button_frame,
    text="+",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press(("+")),
)
button4 = Button(
    button_frame,
    text="4",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((4)),
)
button5 = Button(
    button_frame,
    text="5",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((5)),
)
button6 = Button(
    button_frame,
    text="6",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((6)),
)
substract = Button(
    button_frame,
    text="-",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press(("-")),
)
button7 = Button(
    button_frame,
    text="7",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((7)),
)
button8 = Button(
    button_frame,
    text="8",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((8)),
)
button9 = Button(
    button_frame,
    text="9",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((9)),
)
multiply = Button(
    button_frame,
    text="x",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press(("*")),
)
button0 = Button(
    button_frame,
    text="0",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((0)),
)
decimal = Button(
    button_frame,
    text=".",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press((".")),
)
clear_button = Button(
    button_frame,
    text="C",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=clear,
)
division = Button(
    button_frame,
    text="/",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=lambda: press(("/")),
)
equal = Button(
    button_frame,
    text="=",
    font=("times new roman", 12),
    relief="ridge",
    bd=1,
    bg="#ffffff",
    width=8,
    height=3,
    command=equalpress,
)
expression_field.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=25, pady=5)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
add.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
substract.grid(row=2, column=3)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)
button0.grid(row=4, column=1)
decimal.grid(row=4, column=0)
clear_button.grid(row=4, column=2)
division.grid(row=4, column=3)
buttonsin.grid(row=5, column=0)
buttoncos.grid(row=5, column=1)
buttonlog.grid(row=5, column=2)
equal.grid(row=5, column=3)
window.mainloop()
