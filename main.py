from tkinter import *

window = Tk()
window.title("Convert miles for Km")
my_label = Label(text="My label")
window.config(pady=20,padx=20)

def conversion():
    value = float(miles.get())
    quilometros = round(value * 1.6)
    default.config(text=f"{ quilometros}")

# entry miles value
miles = Entry(width=10)
miles.grid(column=1,row=0)

# text
text_miles = Label(text="Miles")
text_miles.grid(column=2,row=0)

# text of result
result = Label(text="is equal to ")
result.grid(column=0,row=1)
km = Label(text="Km")
km.grid(column=2,row=1)

# value default
default = Label(text="0")
default.grid(column=1,row=1)

#create button
click_convert = Button(text="Convert",command=conversion)
click_convert.grid(column=1,row=3)













window.mainloop()