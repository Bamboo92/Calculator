from tkinter import *

root = Tk()
root.title("Rechner")
root.iconbitmap("icon.ico")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "Beispiel")

def button_click(number):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, bg="#999", command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, bg="#999", command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, bg="#999", command=lambda: button_click(3)).grid(row=3, column=2)

button_4 = Button(root, text="4", padx=40, pady=20, bg="#999", command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, bg="#999", command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, bg="#999", command=lambda: button_click(6)).grid(row=2, column=2)

button_7 = Button(root, text="7", padx=40, pady=20, bg="#999", command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, bg="#999", command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, bg="#999", command=lambda: button_click(9)).grid(row=1, column=2)

button_0 = Button(root, text="0", padx=40, pady=20, bg="#999", command=lambda: button_click(0)).grid(row=4, column=0)

button_equal = Button(root, text="=", padx=87.2, pady=20, bg="#eb582f", command=button_equal).grid(row=4, column=1,columnspan=2)

button_clear = Button(root, text="C", padx=20, pady=20, bg="#f2c200", command=button_clear).grid(row=1, column=3)
button_plus = Button(root, text="+", padx=20, pady=20, fg="#fff", bg="#333", command=button_plus).grid(row=2, column=3)
button_minus = Button(root, text="-", padx=22, pady=20, fg="#fff", bg="#333", command=button_minus).grid(row=3, column=3)


#myButton = Button(root, text="Insert", command=myClick, fg="#00ff00", bg="#222222")#, padx=25, pady=25)
#myButton.pack()


root.mainloop()