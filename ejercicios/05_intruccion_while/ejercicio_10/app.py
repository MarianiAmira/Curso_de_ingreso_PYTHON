import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
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
        numeros = []
        suma_positivo = 0
        suma_negativo = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        while True:
            numero_txt = prompt(title="numero", prompt="Ingrese un número: ")
            
            if numero_txt == "":
                break
            else:
                numero_int = int(numero_txt)
                numeros.append(numero_int)

                if numero_int > 0:
                    suma_positivo += numero_int
                    cantidad_positivos += 1
                elif numero_int < 0:
                    suma_negativo += numero_int
                    cantidad_negativos += 1
                else:
                    cantidad_ceros += 1
            
        diferencia = cantidad_positivos - cantidad_negativos
         
        mensaje_suma = "La suma de positivos es: {0}".format(suma_positivo)
        mensaje_resta = "La suma de positivos es: {0}".format(suma_negativo)
        mensaje_cantidad_positivo = "La cantidad de positivos es: {0}".format(cantidad_positivos)
        mensaje_cantidad_negativo = "La cantidad de negativos es: {0}".format(cantidad_negativos)
        mensaje_cantidad_ceros = "La cantidad de ceros es: {0}".format(cantidad_ceros)
        mensaje_diferencia = "La suma de positivos es: {0}".format(diferencia)
        
        alert(title="Suma de +", message= mensaje_suma)
        alert(title="Suma de -", message= mensaje_resta)
        alert(title="Cantidad de +", message= mensaje_cantidad_positivo)
        alert(title="Cantidad de -", message= mensaje_cantidad_negativo)
        alert(title="Cantidad de 0", message= mensaje_cantidad_ceros)
        alert(title="Diferencia entre + y -", message= mensaje_diferencia)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
