import tkinter 
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")#LABEL, DONDE APARECE UN TEXTO(etiqueta)
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)#CAJITA DE TEXTO
        self.txt_nombre.grid(row=0, column=1)
        
        #self.label2 = customtkinter.CTkLabel(master=self, text="Apellido")
        #self.label2.grid(row=0, column=0, padx=20, pady=10)
        
        #self.txt_apellido = customtkinter.CTkEntry(master=self)#CAJITA DE TEXTO
        #self.txt_apellido.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)#BOTON
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre= self.txt_nombre.get()#OBTENER EL CONTENIDO DE LA CAJA
        saludo="hola {0}".format(nombre)
        alert(title="Saludo ", message=saludo)
                
    
if __name__ == "__main__":
    app = App()
    app.mainloop()