from tkinter import*
# window
window = Tk()
window.title("miles to km converter")
window.minsize(width=400, height=300)
window.config(padx=30,pady=30)

# Entry
input = Entry(width=10)
input.grid(column=2, row=1)

# labels
miles = Label(text="miles", font=("Arial", 16, "bold"))
miles.grid(column=3, row=1)

is_equal_to = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to.grid(column=1, row=2)

km = Label(text="km", font=("Arial", 16, "bold"))
km.grid(column=3, row=2)

answer = Label(text="0", font=("Arial", 16, "bold"))
answer.grid(column=2, row=2)

def miles_km_converter():
    mi_les = float(input.get())
    k_m = mi_les * 1.60934
    answer.config(text=f"{k_m}")


button = Button(text="calculate" , comman =miles_km_converter)
button.grid(column=2, row=3)

window.mainloop()