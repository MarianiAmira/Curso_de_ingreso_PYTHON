import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: intruccion_while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
       respuesta = "Si"
       acumular_positivos = 0
       acumular_negativos = 0
       cantidad_positivos = 0
       cantidad_negativos = 0
       cantidad_ceros = 0
       diferencia = 0

       while respuesta != None:
           numero_ingresado = int(prompt(title="Numeros", prompt="Ingrese un numero"))

           if numero_ingresado > 0:
               acumular_positivos += numero_ingresado
               cantidad_positivos += 1
           elif numero_ingresado < 0:
                acumular_negativos += numero_ingresado
                cantidad_negativos += 1
           elif numero_ingresado == 0:
               cantidad_ceros += 1

           respuesta = prompt(title="Pregunta", prompt="Quiere ingresar otro numero?")

       diferencia = cantidad_positivos - cantidad_negativos
       
       mensaje = "La suma de los positivos es : {0}\nLa suma de los negativos es: {1}\nLa cantidad de positivos es de: {2}\nLa cantidad de negativos es de: {3}\nLa cantidad de ceros es de: {4}\nLa diferencia entre la cantidad de positivos y negativos es de: {5}".format(acumular_positivos, acumular_negativos,cantidad_positivos,cantidad_negativos,cantidad_ceros,diferencia)
       
       alert(title="Respuestas", message=mensaje)

    
if __name__ == "__main__":
    app = App()
    app.mainloop() 
 