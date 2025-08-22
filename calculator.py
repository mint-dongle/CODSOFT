import tkinter as tk
from tkinter import ttk

def handle_button(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            #replace symbols with python operators
            expression = current_text.replace("÷", "/").replace("×", "*")
            result = eval(expression)

            #check for a whole number
            if result.is_integer():
                result = int(result)

            result_var.set(result)
        except Exception as e:
            result_var.set("Error")

    elif clicked_button_text == "C":
            result_var.set("") 
    elif clicked_button_text == "%":
        #Convert the current number to decimal by dividing it by 100
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    
    elif clicked_button_text == "±":
        #covert the current number to its negative
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except  ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)   

#create the main window
root = tk.Tk()
root.title("CALCULATOR")    

result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font=("Display", 50), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# buttons layout
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]
# add colours
#style for theme
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Display", 20), width=8, height=8)
button_colors = {
    "C":{"bg": "#eb3b5a", "fg": "white"},
    "±":{"bg": "#eb3b5a", "fg": "white"},
    "%":{"bg": "#eb3b5a", "fg": "white"},
    "÷":{"bg": "#f7b731", "fg": "black"},
    "×":{"bg": "#f7b731", "fg": "black"},
    "-":{"bg": "#f7b731", "fg": "black"},
    "+":{"bg": "#f7b731", "fg": "black"},
    "=":{"bg": "#f7b731", "fg": "black"},
    ".":{"bg": "#d1d8e0", "fg": "black"},
    "0":{"bg": "#d1d8e0", "fg": "black"},
    "1":{"bg": "#d1d8e0", "fg": "black"},
    "2":{"bg": "#d1d8e0", "fg": "black"},
    "3":{"bg": "#d1d8e0", "fg": "black"},
    "4":{"bg": "#d1d8e0", "fg": "black"},
    "5":{"bg": "#d1d8e0", "fg": "black"},
    "6":{"bg": "#d1d8e0", "fg": "black"},
    "7":{"bg": "#d1d8e0", "fg": "black"},
    "8":{"bg": "#d1d8e0", "fg": "black"},
    "9":{"bg": "#d1d8e0", "fg": "black"},
}

for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    color = button_colors.get(button_text, {"bg": "#fff", "fg": "black"})
    button = tk.Button(
        root,
        text=button_text,
        font=("Arial", 20),
        bg=color["bg"],
        fg=color["fg"],
        command=lambda text=button_text: handle_button(text)
    )
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=6, ipady=4)
    
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

width = 500
height = 400
root.geometry(f"{width}x{height}")

root.resizable(False, False)

root.bind("<Return>", lambda event: handle_button("="))
root.bind("<BackSpace>", lambda event: handle_button("C"))

root.mainloop()