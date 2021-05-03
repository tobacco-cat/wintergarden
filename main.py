print("Build 1.89876355; Date 02.05.21; Bulded on 'ASER Aspire 3'; Builded automaticly.; Builded with debug console")
print("Filemanager 1 by ParTy")

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import webbrowser

print("[Log] Program started: Done!")

def open_file():
    filepath = askopenfilename(
        filetypes=[("Пайтон", "*.py"), ("Все файлы", "*.*"), ("Текстовые файлы", "*.txt*")]
    )
    print("[Log] File open!")
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"File manager - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("Пайтон", "*.py"), ("Все файлы", "*.*"), ("Текстовые файлы", "*.txt*")],
    )
    print("[Log] File save!")
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"File manager - {filepath}")

global font
font = "Calibri"
def font1():
    font = "Comic Sans MS"
def font2():
    font = "Forte"

def settings():
    setting = tk.Tk()
    setting.title("Settings")
    setting.columnconfigure(1, minsize=200, weight=1)
    setting.resizable(False, False)

    setting.rowconfigure(0, minsize=200, weight=1)
    setting.columnconfigure([0, 1, 2], minsize=200, weight=1)

    label1 = tk.Label(text="В разработке...", font=("Comic Sans MS", 12, "bold"), master=setting)
    label1.grid(row=0, column=0, sticky="nsew")





def about():
    webbrowser.open("https://github.com/ParTy-Play-go")
def aboutprog():
    webbrowser.open("https://github.com/ParTy-Play-go/filemanager")

window = tk.Tk()
window.title("File manager")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
#  2 Row Main window
btn_increase = tk.Label(master=window, background="gray7", text="(C) Party;", foreground="gray14", font=("Calibri", 10, "bold"))
btn_increase.grid(row=2, column=0, sticky="nsew")
btn_in = tk.Label(master=window, background="gray7", text=" Build 1.89876355", foreground="gray14", font=("Calibri", 10, "bold"))
btn_in.grid(row=3, column=0, sticky="nsew")
#  2 row main window
txt_edit = tk.Text(window, background="gray18", foreground="darkolivegreen1", font=font)
fr_buttons = tk.Frame(window, relief=tk.FLAT, bd=2, background="gray7")
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file, relief=tk.FLAT)
btn_save = tk.Button(fr_buttons, text="Сохранить как...", command=save_file, relief=tk.FLAT)
btn_settin = tk.Button(fr_buttons, text="Настройки", command=settings, relief=tk.FLAT)
btn_about = tk.Button(fr_buttons, text="Гитхаб Автора", relief=tk.FLAT, command=about)
btn_aboutproject = tk.Button(fr_buttons, text="Гитхаб Проекта", relief=tk.FLAT, command=aboutprog)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_settin.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_about.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_aboutproject.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


txt_edit.scroll_x = tk.Scrollbar(window, orient=tk.HORIZONTAL)
txt_edit.scroll_y = tk.Scrollbar(window, orient=tk.VERTICAL)
txt_edit.canvas = tk.Canvas(window, width=300, height=100,
                                  xscrollcommand=txt_edit.scroll_x.set,
                                  yscrollcommand=txt_edit.scroll_y.set)
txt_edit.scroll_x.config(command=txt_edit.canvas.xview)
txt_edit.scroll_y.config(command=txt_edit.canvas.yview)

label4 = tk.Label(window, background="gray18", foreground="white", text="Тут будут кнопки для удобства... Тоже в разработке...", font=("Calibri", 16, "bold"))
label4.grid(row=2, column=1, sticky="nsew")
label5 = tk.Label(window, background="gray18")
label5.grid(row=3, column=1, sticky="nsew")


window.mainloop()
