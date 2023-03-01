from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=200, height=200)

# Entries
mile_input = Entry(width=9)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

# Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="Is equal to: ")
equal_label.grid(column=0, row=1)

variable_label = Label(text='0')
variable_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)


# Buttons
def calculate():
    user_input = float(mile_input.get())
    variable_label.config(text=round(user_input * 1.689, 2))


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
