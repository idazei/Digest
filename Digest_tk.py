from ensurepip import bootstrap
from tkinter import OptionMenu, StringVar
from tkinter.ttk import Menubutton

import ttkbootstrap as ttk

def close_func():
    print("Closing...")
    app.destroy()

def save_func():
    print("Saving...")
    app.destroy()

#def retrieve_input():
#    input = name_frame.get("1.0",END)
#    return input

def device(X):
    print(x)

app = ttk.Window(themename="cyborg")
app.geometry("400x400")

label = ttk.Label(app, text="Digest")
label.pack(pady=5)
label.config(font=("Arial", 20, "bold"))

name_frame = ttk.Frame(app)
name_frame.pack(pady=10, padx=10, fill="x")
ttk.Label(name_frame, text="NSN:").pack(side="left", padx=5)
ttk.Entry(name_frame).pack(side="left", fill="x", expand=True, padx=35)

company_frame = ttk.Frame(app)
company_frame.pack(pady=10, padx=10, fill="x")
ttk.Label(company_frame, text="Device:").pack(side="left", padx=4)
ttk.Entry(company_frame).pack(side="left", fill="x", expand=True, padx=27)

phone_frame = ttk.Frame(app)
phone_frame.pack(pady=10, padx=10, fill="x")
ttk.Label(phone_frame, text="Name:").pack(side="left", padx=4)
ttk.Entry(phone_frame).pack(side="left", fill="x", expand=True, padx=27)

checkbox_frame = ttk.Frame(app)
checkbox_frame.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(checkbox_frame, bootstyle="round-toggle", text="Remember Info?").pack(side="left", padx=10)

button_frame = ttk.Frame(app)
button_frame.pack(pady=30, padx=10, fill="x")
ttk.Button(button_frame, text="Submit", bootstyle="success", command = lambda: save_func()).pack(side="left", padx=10)
ttk.Button(button_frame, text="Cancel", bootstyle="secondary", command = lambda: close_func()).pack(side="left", padx=22)

app.mainloop()