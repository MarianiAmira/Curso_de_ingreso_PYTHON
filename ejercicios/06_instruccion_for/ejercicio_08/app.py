import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt(title="Numero", prompt="Ingrese un numero"))
        es_primo = True
        if numero < 2:
            es_primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
                    break

        if es_primo:
            mensaje = "{0} es primo".format(numero)
        else:
            mensaje = "{0} no es primo".format(numero)

        alert(title="Numero", message=mensaje)

        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()