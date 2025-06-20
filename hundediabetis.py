import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont


def validate_float(input :str) -> bool:    # validate the user input in the Entry field
    if input == "":
        return True
    try:
        float(input)
    except:
        return False
    return True

def submit():
    global ivl  # insulin value label 
    mmol = float(userinput.get().strip())
    if mmol > 18:   # check for diabetes value
        value = 16
    elif mmol > 14:
        value = 14
    elif mmol > 12:
        value = 12
    elif mmol > 10:
        value = 10
    elif mmol > 8:
        value = 8
    else:
        value = 0
    if ivl is None:
        ivl = tk.Label(outer_frame, text=f'Der zu spritzende Insulinwert ist: {value}',bg='#3C8B7B')
        ivl.pack()
    else:
        ivl.config(text=f'Der zu spritzende Insulinwert ist: {value}')

ivl = None    
root = tk.Tk()  # create application window
root.title('Tinker test App') # app title
root.config(bg="#201C1C")
root.bind('<Return>', submit())

window_width = 500  # width for the app 
window_height= 500  # height for the app
screen_width = root.winfo_screenwidth() #get user max screenwidht
screen_height = root.winfo_screenheight()   #get user max screenheight

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')    # display window

outer_frame = tk.Frame(root, height=400, width=400, highlightbackground='black',highlightthickness=2)
outer_frame.config(bg="#3C8B7B")
outer_frame.place(relx=.5,rely=.5, anchor='center')
outer_frame.pack_propagate(False)

text = ttk.Label(outer_frame,text='Gib die Diabetiswerte ein',font=tkFont.Font(size=22),background='#3C8B7B')# text for input field
userinput = tk.StringVar()  # create var to store input
input_field = ttk.Entry(outer_frame,validate='key', validatecommand=(root.register(validate_float),'%P'),textvariable=userinput)    # user input field | link stringvar to it
diabetes_btn = ttk.Button(outer_frame,text='Eingabe',command=submit)

text.pack(pady=10) 
input_field.pack(pady=5)
diabetes_btn.pack(pady=5)
input_field.focus()  # entry field focused on start

root.mainloop() # execute propgramm 