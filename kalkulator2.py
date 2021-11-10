import tkinter

root = tkinter.Tk()
root.title("Kalkulator")

expression = ""


def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
            

label_result = tkinter.Label(root, height=3, font=24, text="")
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1", width=5, height=2, command=lambda: add("1"), font=14)
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", width=5, height=2, command=lambda: add("2"), font=14)
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", width=5, height=2, command=lambda: add("3"), font=14)
button_3.grid(row=1, column=2)

button_4 = tkinter.Button(root, text="4", width=5, height=2, command=lambda: add("4"), font=14)
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", width=5, height=2, command=lambda: add("5"), font=14)
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", width=5, height=2, command=lambda: add("6"), font=14)
button_6.grid(row=2, column=2)

button_7 = tkinter.Button(root, text="7", width=5, height=2, command=lambda: add("7"), font=14)
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8", width=5, height=2, command=lambda: add("8"), font=14)
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9", width=5, height=2, command=lambda: add("9"), font=14)
button_9.grid(row=3, column=2)

button_clear = tkinter.Button(root, text="C", width=5, height=2, command=lambda: clear(), font=14)
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, text="0", width=5, height=2, command=lambda: add("0"), font=14)
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", width=5, height=2, command=lambda: add("."), font=14)
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", width=5, height=2, command=lambda: add("+"), font=14)
button_add.grid(row=4, column=3)

button_minus = tkinter.Button(root, text="-", width=5, height=2, command=lambda: add("-"), font=14)
button_minus.grid(row=3, column=3)

button_divide = tkinter.Button(root, text="/", width=5, height=2, command=lambda: add("/"), font=14)
button_divide.grid(row=1, column=3)

button_multiply = tkinter.Button(root, text="*", width=5, height=2, command=lambda: add("*"), font=14)
button_multiply.grid(row=2, column=3)

button_open = tkinter.Button(root, text="(", width=5, height=2, command=lambda: add("("), font=14)
button_open.grid(row=5, column=2)

button_close = tkinter.Button(root, text=")", width=5, height=2, command=lambda: add(")"), font=14)
button_close.grid(row=5, column=3)

button_equals = tkinter.Button(root, text="=", width=11, height=2, command=lambda: calculate(), font=14)
button_equals.grid(row=5, column=0, columnspan=2)

root.mainloop()