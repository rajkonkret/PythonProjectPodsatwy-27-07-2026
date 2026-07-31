# tkinter, pyQt, PySide, gtk+, customtkinter
import tkinter


class MyGui:
    """
    Okienko
    """

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Kurs Python")
        self.main_window.geometry("640x480")

        self.label1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Python")
        self.label3 = tkinter.Label(self.main_window, text="Top")
        self.label4 = tkinter.Label(self.main_window, text="Bottom")

        self.label1.pack(side="left")
        self.label2.pack(side="right")
        self.label3.pack(side="top")
        self.label4.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()


my_gui = MyGui()
