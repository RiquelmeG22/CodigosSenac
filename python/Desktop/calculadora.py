import tkinter as tk 

def calculadora(operation):
    global expression

    if operation == "C":
        expression == ""
    elif operation == "B":
        expression = expression [: -1]
    else:
        if expression == "" and operation in ['+', '-', '*', '/']:
            return
        expression += operation
    
    label_text.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        label_text.set(result)
        expression = result
    except:
        label_text.set("Error")
        expression = ""

root = tk.Tk()
root.title("Calculadora")

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.columnconfigure(3, weight=1)
expression = ""
label_text = tk.StringVar()
label_text.set(expression)
root.geometry('400x500')
root.resizable(False, False)

label = tk.Label(root, textvariable=label_text, font=('Arial', 30), bg='white')
label.grid(row=0, column=0, columnspan=4, sticky='we')

botao = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('C', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('B', 4, 2), ('*', 4, 3),
    ('/', 5, 0)

  
]

for text, row, col in botao:
    action = lambda x=text: calculadora(x) if x != '=' else evaluate
    button = tk.Button(root, text=text, command=action, font=('Arial', 15), background='purple')
    button.grid(row=row, column=col, sticky='we')

button = tk.Button(root, text='=', command=evaluate, font=('Arial', 15))
button.grid(row=6, column=1, columnspan=2, sticky='we')

root.mainloop()
