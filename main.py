from tkinter import *
from PIL import ImageTk, Image

# UI
window = Tk()
window.title("Secrets Notes")
window.geometry("500x700")
window.config(bg="light blue", padx=20, pady=20)

bg_color = "light blue"
font_ = ('Source Serif Pro', 10, 'bold')
font_button = ('Source Serif Pro', 10, 'normal')
logo = ImageTk.PhotoImage(Image.open('top_secret.png'))
logo_label = Label(image=logo, width=200, height=200, bg=bg_color)
logo_label.pack()

maste_key_label = Label(text="Enter your notes title", bg=bg_color, font=font_, padx=5, pady=5)
maste_key_label.pack()
master_key_entry = Entry(width=30, border=2)
master_key_entry.pack()

text_label = Label(text="enter your secret notes", bg=bg_color, font=font_, padx=5, pady=5)
text_label.pack()
text_entry = Text(width=45, height=15)
text_entry.pack()

master_key_label = Label(text="Enter master key", bg=bg_color, font=font_, padx=5, pady=5)
master_key_label.pack()
master_key_entry = Entry(width=30, border=2)
master_key_entry.pack(pady=5)

save_button = Button(text="Save & Encrypt", font=('Source Serif Pro', 10, 'normal'),width=13,pady=5)
save_button.pack(pady=5)

decrypt_button = Button(text="Decrypt", font=('Source Serif Pro', 10, 'normal'),width=13,pady=5)
decrypt_button.pack()

mainloop()