import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cantidad_divisores = 0
        numeros= int(prompt(title="Numero", prompt="Ingresa un numero"))
        for i in range(1, numeros):
            if numeros % 1 == 0:
                cantidad_divisores += 1
        mensaje = "Los numeros divisores son: {0}\nCantidad de numeros divisores son: {1}".format(numeros, cantidad_divisores)
        alert(title="Numeros divisores", message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()