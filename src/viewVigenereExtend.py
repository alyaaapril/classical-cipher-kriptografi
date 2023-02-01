from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img/frame-vigenere-extend")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back():
    from viewMainPage import mainPage
    mainPage(window)

def clickVigenere():
    from viewVigenere import vigenereCipher
    vigenereCipher(window)

def clickPlayfair():
    from viewPlayfairCip import playfairCipher
    playfairCipher(window)

def clickOTP():
    from viewOTP import otpCipher
    otpCipher(window)


class vigenereCipherExtend():
    def __init__(self, screen):
        self.screen = screen
        screen.destroy()
        global window
    
        window = Tk()
        window.title("Extend Vigenere Cipher")
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
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=106.0,
            y=359.0,
            width=158.0,
            height=31.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=425.0,
            y=360.0,
            width=120.0,
            height=31.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            323.5,
            254.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#E4E4E7",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=110.0,
            y=157.0,
            width=427.0,
            height=192.0
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
            x=444.0,
            y=434.0,
            width=101.0,
            height=44.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            269.0,
            458.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#E4E4E7",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=113.0,
            y=438.0,
            width=312.0,
            height=38.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=635.0,
            y=377.0,
            width=171.0,
            height=31.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=967.0,
            y=378.0,
            width=120.0,
            height=31.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            600.0,
            47.0,
            image=image_image_1
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickVigenere(),
            relief="flat"
        )
        button_6.place(
            x=503.0,
            y=58.0,
            width=144.0,
            height=37.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickPlayfair(),
            relief="flat"
        )
        button_7.place(
            x=892.0,
            y=58.0,
            width=134.0,
            height=37.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: clickOTP(),
            relief="flat"
        )
        button_8.place(
            x=1042.0,
            y=58.0,
            width=134.0,
            height=37.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=663.0,
            y=58.0,
            width=213.0,
            height=37.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            861.0,
            261.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#E4E4E7",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=643.0,
            y=152.0,
            width=436.0,
            height=217.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: back(),
            relief="flat"
        )
        button_10.place(
            x=69.0,
            y=536.0,
            width=101.0,
            height=44.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            692.0,
            136.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            180.0,
            421.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            151.0,
            141.0,
            image=image_image_4
        )
        window.resizable(False, False)
        window.mainloop()
