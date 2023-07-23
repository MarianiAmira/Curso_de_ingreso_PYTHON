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
            respuesta = prompt(title="Pregunta", prompt="Quiere ingresar otro numero?")

    def btn_mostrar_estadisticas_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0
        numero_minimo = 0
        numero_maximo = 0

        for numeros in self.lista_datos_numeros:
            if numeros < 0:
                acumulador_negativos += numeros
                contador_negativos += 1
            elif numeros > 0:
                acumulador_positivos += numeros
                contador_positivos += 1
            else:
                contador_ceros += 1

            if numeros < numero_minimo:
                numero_minimo = numeros

            if numeros > numero_maximo:
                numero_maximo = numeros

        promedio_negativos = acumulador_negativos / contador_negativos

        mensaje = "La suma acumulada de los negativos es de: {0}\nLa suma acumulada de los positivos es de:{1}\nLa cantidad de numeros negativos es de {2}\nLa cantidad de numeros positivos es de {3}\nLa cantidad de ceros es de: {4}\nEl numero minimo de numeros negativos es: {5}\nEl numero maximo de positivos es: {6}\nEl promedio de numero negativos es: {7}".format(acumulador_negativos,acumulador_positivos,contador_negativos,contador_positivos,contador_ceros,numero_minimo, numero_maximo,promedio_negativos)

        alert(title="Resultados", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
