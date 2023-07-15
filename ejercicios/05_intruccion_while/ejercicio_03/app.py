import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Amira
apellido: Mariani
---
Ejercicio: instruccion_while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        clave_ingresada = prompt(title="Clave", prompt="Ingrese la clave")
        while clave_ingresada != "utn750":
            clave_ingresada = prompt(title="ERROR", prompt="ERROR, intente otra vez")

        alert(title="Clave", message="Clave correcta")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()