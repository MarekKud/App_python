
from tkinter import*
from tkinter import messagebox
import tkinter
import tkinter.font as tkFont
import random


class App:
    def __init__(self, root):
        # setting title
        root.title("First app *Virus*")
        # setting window size
        width = 400
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_707 = Button(root)
        GButton_707["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        GButton_707["font"] = ft
        GButton_707["fg"] = "#000000"
        GButton_707["justify"] = "center"
        GButton_707["text"] = "Push"
        GButton_707.place(x=140, y=160, width=124, height=30)
        GButton_707["command"] = self.GButton_707_command

        GButton_796 = Button(root)
        GButton_796["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        GButton_796["font"] = ft
        GButton_796["fg"] = "#000000"
        GButton_796["justify"] = "center"
        GButton_796["text"] = "Close window"
        GButton_796.place(x=270, y=350, width=120, height=30)
        GButton_796["command"] = self.GButton_796_command

        self.GLineEdit_577 = Entry(root)
        self.GLineEdit_577["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.GLineEdit_577["font"] = ft
        self.GLineEdit_577["fg"] = "#333333"
        self.GLineEdit_577["justify"] = "center"
        self.GLineEdit_577["text"] = "Wpisz cos"
        self.GLineEdit_577.place(x=20, y=30, width=367, height=30)

        self.GLabel_633 = Label(root)
        ft = tkFont.Font(family='Times', size=14)
        self.GLabel_633["font"] = ft
        self.GLabel_633["fg"] = "#333333"
        self.GLabel_633["bg"] = "#cc0000"
        self.GLabel_633["justify"] = "center"
        self.GLabel_633["text"] = "**Danger**"
        self.GLabel_633.place(x=170, y=130, width=70, height=25)

        GLabel_634 = Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_634["font"] = ft
        GLabel_634["fg"] = "#333333"
        GLabel_634["bg"] = "#fad400"
        GLabel_634["justify"] = "center"
        GLabel_634["text"] = "Enter something "
        GLabel_634.place(x=110, y=3, width=200, height=25)

    def GButton_707_command(self):

        input = self.GLineEdit_577.get()
        try:
            if len(input) == 0:
                raise Exception

        except Exception:
                messagebox.showinfo("Empty field", "Give data")
        else:
            print(input)
            self.GLineEdit_577.delete(0, tkinter.END)
            i = 0
            while i < 300:
                random.seed()
                x1 = random.randint(0, 400)
                y1 = random.randint(0, 400)

                lbl3 = Label(root, text=chr(0x1f630)*10, bg="#ff8c00")
                lbl3.place(x=x1, y=y1, width=70, height=25)
                i += 1
            

    def GButton_796_command(self):
        x = messagebox.askyesno("Close window", "Are you sure")
        if x:
            root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
