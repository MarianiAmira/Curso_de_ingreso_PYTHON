import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: instruccion_while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        respuesta = "Si"
        '''bandera, concepto para que tenga dos conceptos'''
        bandera_del_primero = False

        while respuesta != None:

            numero_ingresado = prompt(title="Numero", prompt="Ingrese un numero")

            if bandera_del_primero == False: #carga el primer numero para q en la segunda vuelta los compare
                numeros_maximo = numero_ingresado
                numero_minimo = numero_ingresado #el primer numero que ingresa es minimo y maximo, para asegurar el max y min
                bandera_del_primero = True #se levanta la bandera en la segunda vuelta
            else:
                if numero_ingresado > numeros_maximo:
                    numeros_maximo = numero_ingresado
                if numero_ingresado < numero_minimo:
                    numero_minimo = numero_ingresado
            
            respuesta = prompt(title="Numero", prompt="Desea ingresar otro numero")
        
        self.txt_minimo.delete(0, 1000)
        self.txt_minimo.insert(0, numero_minimo)
        self.txt_maximo.delete(0, 1000)
        self.txt_maximo.insert(0, numeros_maximo)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
