from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img/frame-main")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Declare the Button
def clickVigenere():
    from viewVigenere import vigenereCipher
    vigenereCipher(window)

def clickVigenereExtend():
    from viewVigenereExtend import vigenereCipherExtend
    vigenereCipherExtend(window)

def clickPlayfair():
    from viewPlayfairCip import playfairCipher
    playfairCipher(window)

def clickOTP():
    from viewOTP import otpCipher
    otpCipher(window)


def mainPage(screen=None):
    if (screen != None):
        screen.destroy()
    global window
    window = Tk()
    window.title("Classical Cipher")
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
        320.0,
        390.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1108.0,
        539.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1150.0,
        39.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        1068.0,
        116.0,
        1223.0,
        251.0,
        fill="#D3C3B1",
        outline="")

    canvas.create_rectangle(
        897.0,
        540.0,
        1119.0,
        675.0,
        fill="#D3C3B1",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clickPlayfair(),
        relief="flat"
    )
    button_1.place(
        x=123.0,
        y=349.0,
        width=253.0,
        height=118.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clickOTP(),
        relief="flat"
    )
    button_2.place(
        x=409.0,
        y=349.0,
        width=253.0,
        height=118.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clickVigenere(),
        relief="flat"
    )
    button_3.place(
        x=123.0,
        y=197.0,
        width=253.0,
        height=118.0
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
        x=409.0,
        y=197.0,
        width=253.0,
        height=118.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    mainPage()