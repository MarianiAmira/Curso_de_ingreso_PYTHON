import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista_datos_numeros = []

    def btn_comenzar_ingreso_on_click(self):
        respuesta = "Si"
        while respuesta != None:
            numeros_ingresados = int(prompt(title="Numeros", prompt="Ingrese un numero"))
            self.lista_datos_numeros.append(int(numeros_ingresados))
            respuesta = prompt(title="Numeros", prompt="Quiere ingresar otro numero")

    def btn_mostrar_estadisticas_on_click(self):
        suma_positivos = 0
        cantidad_positivos = 0
        suma_negativos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        minimo_negativos = None
        maximo_positivos = None
        promedio = 0

        for numeros_ingresados in self.lista_datos_numeros:
            if numeros_ingresados > 0:
                suma_positivos += numeros_ingresados
                cantidad_positivos += 1
                if maximo_positivos is None or numeros_ingresados > maximo_positivos:
                    maximo_positivos = numeros_ingresados
            elif numeros_ingresados < 0:
                suma_negativos += numeros_ingresados
                cantidad_negativos += 1
                if minimo_negativos is None or numeros_ingresados < minimo_negativos:
                    minimo_negativos = numeros_ingresados
            else:
                cantidad_ceros += 1

            if cantidad_negativos > 0:
                promedio = suma_negativos / cantidad_negativos

        mensaje = "La suma acumulada de los negativos es {0}\nLa suma acumulada de los positivos {1}\nCantidad de números positivos ingresados {2}\nCantidad de números negativos ingresados {3}\nCantidad de ceros {4}\nEl minimo de los negativos {5}\nEl maximo de los positivos {6}\nEl promedio de los negativos {7}".format(suma_negativos,suma_positivos,cantidad_positivos,cantidad_negativos,cantidad_ceros,minimo_negativos,maximo_positivos,promedio)   

        alert(title="Resultados", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
