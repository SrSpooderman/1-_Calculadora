#importaciones
from tkinter import *
from math import *
#definisiones
def btnClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
#funsiones
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador=""
#limpiesa
def clear():
    global operador
    operador=""
    input_text.set("0")

#ventana
ventana=Tk()
ventana.title("Le Calculatriz")
ventana.geometry("392x500")
ventana.configure(background='#463C3C')
#botones epicos
##tamaño de los botones
ancho_boton=11
alto_boton=3
color_boton=("#393939")
#variable botones
input_text=StringVar()
operador=""
#pantallica
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="#B30D0D",justify="right").place(x=10,y=60)
#le botone
Boton0=Button(ventana,text='0',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(0)).place(x=17,y=180)
Boton1=Button(ventana,text='1',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(1)).place(x=107,y=180)
Boton2=Button(ventana,text='2',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(2)).place(x=197,y=180)
Boton3=Button(ventana,text='3',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(3)).place(x=287,y=180)
#
Boton4=Button(ventana,text='4',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(4)).place(x=17,y=240)
Boton5=Button(ventana,text='5',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(5)).place(x=107,y=240)
Boton6=Button(ventana,text='6',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(6)).place(x=197,y=240)
Boton7=Button(ventana,text='7',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(7)).place(x=287,y=240)
#
Boton8=Button(ventana,text='8',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(8)).place(x=17,y=300)
Boton9=Button(ventana,text='9',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick(9)).place(x=107,y=300)
Boton_sum=Button(ventana,text='+',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("+")).place(x=197,y=300)
Boton_res=Button(ventana,text='-',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("-")).place(x=287,y=300)
#
Boton_mult=Button(ventana,text='*',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("*")).place(x=17,y=360)
Boton_div=Button(ventana,text='/',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("/")).place(x=107,y=360)
Boton_exp=Button(ventana,text='EXP',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("**")).place(x=197,y=360)
Botonresul=Button(ventana,text='=',bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=360)
#
Botonlimpiar=Button(ventana,text='clear',bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=17,y=420)

clear()
ventana.mainloop()
