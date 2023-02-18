from tkinter import *

window = Tk()
window.title('TKinter')
window.minsize(width=600, height=600)

my_label = Label(text='My Label', font=('Arial', 22, 'bold'))
my_label.pack()

# my_label['text'] = 'new text'
# my_label.config(text='NEWP TREKSTA')


def button_clicked():
    my_label.config(text=entry.get())


button = Button(text='Click ME', command=button_clicked)
button.pack()

# Entry
entry = Entry(width=10)
entry.pack()





window.mainloop()