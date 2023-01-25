import tkinter as tk
import pyautogui , keyboard
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title('Auto Typer')

# store key  and text
key = tk.StringVar()
text = tk.StringVar()



def ready():
    while True:
        if keyboard.is_pressed(key.get()):
            pyautogui.hotkey('backspace')
            pyautogui.typewrite(text.get())





signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# key
key_label = ttk.Label(signin, text="Key:")
key_label.pack(fill='y', expand=False)

key_entry = ttk.Entry(signin, textvariable=key)
key_entry.pack(fill='x', expand=True)
key_entry.focus()

# text
text_label = ttk.Label(signin, text="Text:")
text_label.pack(fill='y', expand=True)

text_entry = ttk.Entry(signin, textvariable=text)
text_entry.pack(fill='x', expand=True)

# ready button
ready_button = ttk.Button(signin, text="Ready", command=ready)
ready_button.pack(fill='x', expand=True, pady=3)
ready_button.pack()

root.mainloop()
