import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: listas_02
---
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1, 2, 3]


    def btn_mostrar_on_click(self):
        numero_uno = int(prompt(title="Numero 1", prompt="Ingrese un numero: "))
        numero_dos = int(prompt(title="Numero 2", prompt="Ingrese un numero: "))
        numero_tres = int(prompt(title="Numero 3", prompt="Ingrese un numero: "))

        self.lista_datos_uno = [numero_uno]
        self.lista_datos_dos = [numero_dos]
        self.lista_datos_tres = [numero_tres]
         
    def btn_cargar_on_click(self):
            alert(title="Numero Ingresados", message= self.lista_datos_uno)
            alert(title="Numero Ingresados", message= self.lista_datos_dos)
            alert(title="Numero Ingresados", message= self.lista_datos_tres)
 
    
if __name__ == "__main__":
    app = App()
    app.mainloop()