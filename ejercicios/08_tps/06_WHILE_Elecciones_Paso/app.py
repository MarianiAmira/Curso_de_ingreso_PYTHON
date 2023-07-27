'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        respuesta = "Si"
        candidato_mas_votos = 0
        nombre_candidato_mas_votos = ""
        nombre_candidato_menos_votos = None
        candidato_menos_votos = float('inf')
        edad_candidato_menos_votos = -1
        contador_edades_candidatos = 0
        acumulador_edades_candidatos = 0
        bandera_candidato_mas_votos = False
        bandera_candidato_menos_votos = False

        while respuesta != None:
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre:")
            while nombre is None:
                nombre = prompt(title="ERROR", prompt="ERROR, Ingrese su nombre:")
            edad = int(prompt(title="Edad", prompt="Ingrese su edad:"))
            while edad < 25:
                edad = int(prompt(title="ERROR", prompt="ERROR, Ingrese su edad:"))
            cantidad_votos = int(prompt(title="Cantidad de votos", prompt="Ingrese la cantidad de votos del candidato:"))
            while cantidad_votos < 0:
                cantidad_votos = prompt(title="ERROR", prompt="ERROR, Ingrese la cantidad de votos del candidato:")

            respuesta= prompt(title="Pregunta", prompt="Quiere ingresar otro candidato?")

            #a. nombre del candidato con más votos
            if bandera_candidato_mas_votos == True:
                candidato_mas_votos = cantidad_votos
                nombre_candidato_mas_votos = nombre
            else:
                if cantidad_votos > candidato_mas_votos:
                    candidato_mas_votos = cantidad_votos
                    nombre_candidato_mas_votos = nombre
                    bandera_candidato_mas_votos = False

            # b. nombre y edad del candidato con menos votos
            if bandera_candidato_menos_votos == True:
                candidato_menos_votos = cantidad_votos
                nombre_candidato_menos_votos = nombre
                edad_candidato_menos_votos = edad
                bandera_candidato_menos_votos = False
            else: 
                if cantidad_votos < candidato_menos_votos:
                    candidato_menos_votos = cantidad_votos
                    nombre_candidato_menos_votos = nombre
                    edad_candidato_menos_votos = edad

            # c. el promedio de edades de los candidatos
            contador_edades_candidatos += 1
            acumulador_edades_candidatos += edad

        promedio_candidatos = acumulador_edades_candidatos / contador_edades_candidatos

        print(f"nombre del candidato con más votos: {nombre_candidato_mas_votos}")
        if contador_edades_candidatos == 0: 
            print("No se ingresaron candidatos.")
        else:
            print(f"nombre del candidato con menos votos es {nombre_candidato_menos_votos} y su edad es {edad_candidato_menos_votos}")
        print(f"el promedio de edades de los candidatos: {promedio_candidatos}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
