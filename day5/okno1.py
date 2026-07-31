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


        self.label1.pack(side="left")

        tkinter.mainloop()


my_gui = MyGui()
