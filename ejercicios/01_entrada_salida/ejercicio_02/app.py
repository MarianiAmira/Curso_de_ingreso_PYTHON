import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Amira
apellido:Mariani
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")#LE PONE EL TITULO A LA VENTANA PRINCIPAL
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)#DECLARAR UN BOTON
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre= prompt(title="Pregunta", prompt="Cual es su nombre?")#CAJITA DE TEXTO - Dialog Prompt
        mensaje= "Hola " + nombre + " ¿como estas?"
        alert(title="INFO", message=mensaje) #Dialog Alert
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()