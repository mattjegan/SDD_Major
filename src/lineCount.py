#!/usr/bin/python
import Tkinter as tk

class App:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Lines")
        self.root.geometry("200x70")
        self.main = tk.Label(text="")
        self.main.pack()
        self.libs = tk.Label(text="")
        self.libs.pack()
        self.cons = tk.Label(text="")
        self.cons.pack()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_lines()
        self.root.mainloop()

    def update_lines(self):
        linecount = 0
        mainFile = open("bw_Main.py", "rU")
        libsFile = open("bw_Lib.py", "rU")
        consFile = open("bw_Cons.py", "rU")
        mains = [line for line in mainFile]
        libs = [line for line in libsFile]
        cons = [line for line in consFile]
        mainFile.close()
        libsFile.close()
        consFile.close()

        self.main.configure(text=("main:", str(len(mains))))
        self.libs.configure(text=("libs:", str(len(libs))))
        self.cons.configure(text=("cons:", str(len(cons))))

        linecount = len(mains) + len(libs) + len(cons)
        self.label.configure(text=("Total:",str(linecount)))
        self.root.after(1000, self.update_lines)

app = App()
root.mainloop()