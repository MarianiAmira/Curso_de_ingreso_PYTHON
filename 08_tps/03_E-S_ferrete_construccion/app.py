import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: ferrete_construccion_03
---
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo_txt = self.txt_largo.get()
        largo_int = float(largo_txt)
        ancho_txt = self.txt_ancho.get()
        ancho_int = float(ancho_txt)

        area = largo_int * ancho_int
        perimetro = 2 * (largo_int + ancho_int)
        quebracho_grueso = (perimetro // 250) + 4 
        quebracho_fino  = (perimetro // 12) - quebracho_grueso
        varillas = (perimetro // 2)
        alambre = perimetro * 7

        mensaje = "El area del terreno es: {0}\nEl perimetro del terreno es de: {1}\nLa cantidad de postes necesarios de quebracho Grueso de 2.4 mts es: {2}\nLa cantidad de postes necesarios de quebracho Fino de 2.2 mts es: {3}\nla cantidad de varillas necesarias son de: {4}\nLa cantidad de alambre necesaria es de: {5}".format(area, perimetro, quebracho_grueso,quebracho_fino,varillas,alambre ) 

        alert(title="Resultado", message=mensaje)
    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
