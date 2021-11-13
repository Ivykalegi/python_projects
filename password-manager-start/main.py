from tkinter import*
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password manager")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
# create image at center of canvas
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=2, row=2)


window.mainloop()