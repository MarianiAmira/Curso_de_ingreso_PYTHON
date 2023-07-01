import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, menor o adolescente (edad entre 13 y 17 años) 
de edad, se deberá informar utilizando el Dialog aler.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_txt= self.txt_edad.get()
        edad_int = float(edad_txt)
        if(edad_int >= 18):
            alert(title="Mayor", message="MAYOR")
        elif(edad_int >= 13 and edad_int <=17):
            alert(title="Adolescente", message="ADOLESCENTE")
        else:
            alert(title="Menor", message="MENOR")
    
        alert(title="Ok", message="OK")#Se ejecuta siempre 
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()