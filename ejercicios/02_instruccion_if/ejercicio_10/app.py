import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Amira
apellido: Mariani
---
Ejercicio: instrucion_if_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        import random
        numero_aleatorio_txt = random.randint(1, 10)
        numero_aleatorio_int = float(numero_aleatorio_txt)
        #alert(message=numero_aleatorio_int)

        if (numero_aleatorio_int >=6 and numero_aleatorio_int <=10):
            mensaje= "Promocion directa, su nota es: " + str(numero_aleatorio_txt)
            alert(title="Promocion", message=mensaje)
        elif (numero_aleatorio_int == 4 or numero_aleatorio_int==5):
            mensaje= "Aprobo, su nota es: " + str(numero_aleatorio_txt)
            alert(title="Aprobado", message=mensaje)
        else:
            mensaje= "Desaprobo, su nota es: " + str(numero_aleatorio_txt)
            alert(title="Desaprobo", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()