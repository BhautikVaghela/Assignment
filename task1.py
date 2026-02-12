from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("400x550")
window.resizable(False, False)
window.config(bg="#2C3E50")


equation = ""

def press(num):
    global equation
    equation = equation + str(num)
    equation_label.set(equation)

def equalpress():
    try:
        global equation
        total = str(eval(equation))
        equation_label.set(total)
        equation = total
    except:
        equation_label.set("Error")
        equation = ""

def clear():
    global equation
    equation = ""
    equation_label.set("")
 
def backspace():
    global equation
    equation = equation[:-1]
    equation_label.set(equation)

equation_label = StringVar()

display = Entry(window, textvariable=equation_label, font=('Arial', 20, 'bold'), 
                bd=10, insertwidth=4, width=14, justify='right', bg="#ECF0F1", fg="#2C3E50")
display.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

button_params = {
    'bd': 3,
    'font': ('Arial', 16, 'bold'),
    'width': 5,
    'height': 2
}

number_bg = "#3498DB"
number_fg = "white"
operator_bg = "#E74C3C"
operator_fg = "white"
special_bg = "#95A5A6"
special_fg = "white"

Button(window, text='C', command=clear, bg=special_bg, fg=special_fg, 
       **button_params).grid(row=1, column=0, padx=5, pady=5)
Button(window, text='⌫', command=backspace, bg=special_bg, fg=special_fg, 
       **button_params).grid(row=1, column=1, padx=5, pady=5)
Button(window, text='%', command=lambda: press('%'), bg=operator_bg, fg=operator_fg, 
       **button_params).grid(row=1, column=2, padx=5, pady=5)
Button(window, text='/', command=lambda: press('/'), bg=operator_bg, fg=operator_fg, 
       **button_params).grid(row=1, column=3, padx=5, pady=5)

Button(window, text='7', command=lambda: press(7), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=2, column=0, padx=5, pady=5)
Button(window, text='8', command=lambda: press(8), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=2, column=1, padx=5, pady=5)
Button(window, text='9', command=lambda: press(9), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=2, column=2, padx=5, pady=5)
Button(window, text='*', command=lambda: press('*'), bg=operator_bg, fg=operator_fg, 
       **button_params).grid(row=2, column=3, padx=5, pady=5)

Button(window, text='4', command=lambda: press(4), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=3, column=0, padx=5, pady=5)
Button(window, text='5', command=lambda: press(5), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=3, column=1, padx=5, pady=5)
Button(window, text='6', command=lambda: press(6), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=3, column=2, padx=5, pady=5)
Button(window, text='-', command=lambda: press('-'), bg=operator_bg, fg=operator_fg, 
       **button_params).grid(row=3, column=3, padx=5, pady=5)

Button(window, text='1', command=lambda: press(1), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=4, column=0, padx=5, pady=5)
Button(window, text='2', command=lambda: press(2), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=4, column=1, padx=5, pady=5)
Button(window, text='3', command=lambda: press(3), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=4, column=2, padx=5, pady=5)
Button(window, text='+', command=lambda: press('+'), bg=operator_bg, fg=operator_fg, 
       **button_params).grid(row=4, column=3, padx=5, pady=5)

Button(window, text='0', command=lambda: press(0), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
Button(window, text='.', command=lambda: press('.'), bg=number_bg, fg=number_fg, 
       **button_params).grid(row=5, column=2, padx=5, pady=5)
Button(window, text='=', command=equalpress, bg="#27AE60", fg="white", 
       **button_params).grid(row=5, column=3, padx=5, pady=5)

window.mainloop()
