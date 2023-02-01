from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img/frame-otp")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back():
    from mainPage import mainPage
    mainPage(window)

def clickVigenere():
    from viewVigenere import vigenereCipher
    vigenereCipher(window)

def clickVigenereExtend():
    from viewVigenereExtend import vigenereCipherExtend
    vigenereCipherExtend(window)

def clickPlayfair():
    from viewPlayfairCip import playfairCipher
    playfairCipher(window)


class otpCipher():
    def __init__(self, screen):
        self.screen = screen
        screen.destroy()
        global window

        window = Tk()
        window.title("One Time Pad")
        window.geometry("1200x630")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 630,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            600.0,
            47.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickVigenere(),
            relief="flat"
        )
        button_1.place(
            x=503.0,
            y=58.0,
            width=144.0,
            height=37.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickPlayfair(),
            relief="flat"
        )
        button_2.place(
            x=892.0,
            y=58.0,
            width=134.0,
            height=37.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=1042.0,
            y=58.0,
            width=134.0,
            height=37.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickVigenereExtend(),
            relief="flat"
        )
        button_4.place(
            x=663.0,
            y=58.0,
            width=213.0,
            height=37.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: back(),
            relief="flat"
        )
        button_5.place(
            x=57.0,
            y=539.0,
            width=101.0,
            height=44.0
        )
        window.resizable(False, False)
        window.mainloop()
