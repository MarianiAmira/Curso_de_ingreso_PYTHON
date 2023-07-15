import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: instruccion_while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0 #cuentan de 1 
        acumulador = 0 #almacena los numeros
        self.txt_suma_acumulada.delete(0, "end")
        self.txt_promedio.delete(0, "end")
        while contador < 5:
            numeros_ingresados= int(prompt(title="Numero", prompt="Ingrese un numero"))
            contador += 1
            acumulador += numeros_ingresados
            
        promedio = acumulador / 5
        
        self.txt_suma_acumulada.insert(0, acumulador)
        self.txt_promedio.insert(0, promedio)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
