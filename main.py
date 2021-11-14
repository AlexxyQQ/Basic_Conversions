from tkinter import *
import math


WIN = Tk()
WIN.geometry("1920x1080+0+0")
WIN.resizable(0, 0)

""" Images """
BG = PhotoImage(file="Assets/Frame 1.png")
Degree_button_image = PhotoImage(file="Assets/Degree Button.png")
Number_button_image = PhotoImage(file="Assets/Number Button.png")
Temp_button_image = PhotoImage(file="Assets/Temp Button.png")
Word_button_image = PhotoImage(file="Assets/Word Button.png")
Degree_element_image = PhotoImage(file="Assets/Degree Frame Element.png")
Temp_element_image = PhotoImage(file="Assets/Temprature Frame Element.png")
Number_element_image = PhotoImage(file="Assets/Number System Elements.png")


""" Background """
Label(WIN, image=BG, bg="blue").place(x=0, y=0)


""" Variables for Degree Conversion """
Radian_inputs = StringVar()
Degree_inputs = StringVar()

""" Variables for Temprature Conversion """
kel_input = StringVar()
cel_input = StringVar()
feh_input = StringVar()

"""Variables for Number System Conversion"""
bina_input = StringVar()
octa_input = StringVar()
dec_input = StringVar()
hexa_input = StringVar()


def Angles():
    Angle_frame = LabelFrame(WIN, width=1313, height=902, bg="#B69900", bd=0)
    Angle_frame.place(x=521, y=85)
    Label(Angle_frame, image=Degree_element_image, bg="#B69900").place(x=151, y=350)

    def conversion_degree(event):
        try:
            a = float(Radian_inputs.get())
            b = math.degrees(a)
            Degree_inputs.set(b)
        except:
            print("failed")

    def conversion_radian(event):
        try:
            a = float(Degree_inputs.get())
            b = math.radians(a)
            Radian_inputs.set(b)
        except:
            print("failed")

    Radian_input = Entry(
        Angle_frame,
        text=Radian_inputs,
        width=11,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    Radian_input.place(x=187, y=380)
    Radian_input.bind("<Return>", conversion_degree)

    Degree_input = Entry(
        Angle_frame,
        text=Degree_inputs,
        width=11,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    Degree_input.place(x=766, y=380)
    Degree_input.bind("<Return>", conversion_radian)


def Temps():
    Temps_frame = LabelFrame(WIN, width=1313, height=902, bg="#B69900", bd=0)
    Temps_frame.place(x=521, y=85)
    Label(Temps_frame, image=Temp_element_image, bg="#B69900").place(x=0, y=343)

    def conversion_celcius(event):
        try:
            c = float(cel_input.get())
            f = (c * 9 / 5) + 32
            k = c + 273.15
            feh_input.set(f)
            kel_input.set(k)

        except:
            print("failed")

    def conversion_kelvin(event):
        try:
            k = float(kel_input.get())
            c = k - 273.15
            f = (c * 9 / 5) + 32
            feh_input.set(f)
            cel_input.set(c)
        except:
            print("failed")

    def conversion_Fahrenheit(event):
        try:
            f = float(feh_input.get())
            c = (f - 32) * 5 / 9
            k = c + 273.15
            cel_input.set(c)
            kel_input.set(k)
        except:
            print("failed")

    Cel = Entry(
        Temps_frame,
        text=cel_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    Cel.place(x=40, y=382)
    Cel.bind("<Return>", conversion_celcius)

    Feh = Entry(
        Temps_frame,
        text=feh_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    Feh.place(x=508, y=382)
    Feh.bind("<Return>", conversion_Fahrenheit)

    Kel = Entry(
        Temps_frame,
        text=kel_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    Kel.place(x=975, y=382)
    Kel.bind("<Return>", conversion_kelvin)


def Numbersys():
    Numb_frame = LabelFrame(WIN, width=1313, height=902, bg="#B69900", bd=0)
    Numb_frame.place(x=521, y=85)
    Label(Numb_frame, image=Number_element_image, bg="#B69900").place(x=464, y=13)

    def conversion_binary(event):
        try:
            b = int(bina_input.get(), 2)
            o = oct(b)
            d = int(bina_input.get(), 2)
            h = hex(b)
            dec_input.set(d)
            hexa_input.set(h.replace("0x", ""))
            octa_input.set(o.replace("0o", ""))

        except:
            print("failed")

    def conversion_ocata(event):
        try:
            o = int(octa_input.get(), 8)
            b = bin(o)
            d = int(octa_input.get(), 8)
            h = hex(o)
            dec_input.set(d)
            hexa_input.set(h.replace("0x", ""))
            bina_input.set(b.replace("0b", ""))
        except:
            print("failed")

    def conversion_dec(event):
        try:
            d = int(dec_input.get())
            b = bin(d)
            o = oct(d)
            h = hex(d)
            octa_input.set(o.replace("0o", ""))
            hexa_input.set(h.replace("0x", ""))
            bina_input.set(b.replace("0b", ""))
        except:
            pass

    def conversion_hexa(event):
        try:
            h = int(hexa_input.get(), 16)
            b = bin(h)
            d = int(hexa_input.get(), 16)
            o = oct(h)
            dec_input.set(d)
            octa_input.set(o.replace("0o", ""))
            bina_input.set(b.replace("0b", ""))
        except:
            pass

    bina = Entry(
        Numb_frame,
        text=bina_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    bina.place(x=520, y=32)
    bina.bind("<Return>", conversion_binary)

    octa = Entry(
        Numb_frame,
        text=octa_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    octa.place(x=520, y=496)
    octa.bind("<Return>", conversion_ocata)

    deca = Entry(
        Numb_frame,
        text=dec_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    deca.place(x=520, y=264)
    deca.bind("<Return>", conversion_dec)

    hexa = Entry(
        Numb_frame,
        text=hexa_input,
        width=8,
        font=("Arial", 50),
        bg="#C4C4C4",
        bd=0,
    )
    hexa.place(x=520, y=728)
    hexa.bind("<Return>", conversion_hexa)


""" Buttons """
Button(
    WIN,
    image=Degree_button_image,
    bg="#06A59B",
    activebackground="#06A59B",
    bd=0,
    command=Angles,
).place(x=65, y=153)

Button(
    WIN,
    image=Temp_button_image,
    bg="#06A59B",
    activebackground="#06A59B",
    bd=0,
    command=Temps,
).place(x=65, y=351)

Button(
    WIN,
    image=Number_button_image,
    bg="#06A59B",
    activebackground="#06A59B",
    bd=0,
    command=Numbersys,
).place(x=65, y=549)

Button(
    WIN, image=Word_button_image, bg="#06A59B", activebackground="#06A59B", bd=0
).place(x=65, y=747)

WIN.mainloop()
