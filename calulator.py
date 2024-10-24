from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):  # Corrected init method
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg="#ccddff", font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Button layout
        buttons = [
            ['(', ')', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['C', '0', '.', '=']
        ]

        # Place buttons using a loop
        for i, row in enumerate(buttons):
            for j, label in enumerate(row):
                if label == 'C':
                                        Button(width=11, height=4, text=label, relief='flat', bg='white', command=self.clear).place(x=j*90, y=350)
                elif label == '=':
                    Button(width=11, height=4, text=label, relief='flat', bg='lightblue', command=self.solve).place(x=j*90, y=350)
                else:
                    Button(width=11, height=4, text=label, relief='flat', bg='white', command=lambda value=label: self.show(value)).place(x=j*90, y=i*75 + 50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            # Replacing 'x' with '*' for multiplication
            result = eval(self.entry_value.replace('x', '*'))
            self.equation.set(result)
        except:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()