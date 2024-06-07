
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\lecturess\odev\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1441.0,
    1024.0,
    fill="#A1B3C2",
    outline="")

canvas.create_rectangle(
    1013.0,
    4.0,
    1169.0,
    289.0,
    fill="#5E697D",
    outline="")

canvas.create_rectangle(
    989.0,
    6.0,
    1343.2433776855469,
    1055.991455078125,
    fill="#747685",
    outline="")

canvas.create_rectangle(
    1215.0,
    106.0,
    1502.7860412597656,
    1034.2744140625,
    fill="#252839",
    outline="")

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
    x=1044.0,
    y=900.0,
    width=379.0,
    height=90.0
)

canvas.create_text(
    1044.0,
    404.0,
    anchor="nw",
    text="“Dreamers” adlı bu uygulama rüyanızı dinleyip yorum yapan yapay zeka destekli bir uygulamadır. Umarım aradığınız cevabı bulabilirsiniz.",
    fill="#FFFFFF",
    font=("IstokWeb BoldItalic", 34 * -1)
)

canvas.create_text(
    1044.0,
    296.0,
    anchor="nw",
    text="Rüyanı anlatmak ister misin ?",
    fill="#FFFFFF",
    font=("IstokWeb Bold", 34 * -1)
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
    x=1021.0,
    y=0.0,
    width=419.0,
    height=90.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    544.0,
    557.0,
    image=image_image_1
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
    x=0.0,
    y=0.0,
    width=419.0,
    height=90.0
)

canvas.create_rectangle(
    -5.0,
    85.0,
    1444.0,
    90.0,
    fill="#697783",
    outline="")

canvas.create_rectangle(
    1016.0,
    -5.0,
    1021.0,
    1024.0,
    fill="#697783",
    outline="")
window.resizable(False, False)
window.mainloop()