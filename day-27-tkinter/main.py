from tkinter import*

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack() # layout

my_label["text"] = "New Text"
my_label.config(text = "New Text")
my_label.grid(column=1,row=1)


# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=4, row=3)
# button

def button_clicked():
    my_label.config(text=input.get())


button = Button(text="click me", command = button_clicked)
# button.pack()
button.grid(column=2, row=2)
# button = Button(text="click me", command = button_clicked)


new_button = Button(text="new button", command = button_clicked)
new_button.grid(column=3, row=1)
window.mainloop()