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
        respuesta = "si"
        bandera_votos = False

        votos_mas_altos = -1
        nombre_candidato_mas_votos = ""
        edad_candidatos_menos_votos = -1
        nombre_candidato_menos_votos = ""
        votos_menos_altos = float("inf")
        suma_edades = 0
        total_candidatos = 0
        votos_totales = 0

        while respuesta != None:
            nombre = prompt(title="Nombre Candidato", prompt="Ingrese su nombre")
            while nombre == "":
                nombre = prompt(title="ERROR", prompt="ERROR, Ingrese su nombre")

            edad = int(prompt(title="Edad", prompt="Ingrese su edad"))
            while edad < 25:
                edad = int(prompt(title="ERROR", prompt="ERROR, Ingrese su edad"))

            cantidad_de_votos = int(prompt(title="Votos", prompt="Ingrese sus votos"))
            while cantidad_de_votos < 0:
                cantidad_de_votos = int(prompt(title="ERROR", prompt="Error, Ingrese sus votos"))

            respuesta = prompt(title="Candidatos", prompt="Quiere agregar otro candidato")
            

        '''for candidatos in candidatos:
            nombre, edad, cantidad_de_votos = candidatos'''

        if bandera_votos == False:
            nombre_candidato_mas_votos = nombre
            nombre_candidato_menos_votos = nombre
            bandera_votos = True
        else:
            if cantidad_de_votos > votos_mas_altos:
                nombre_candidato_mas_votos = nombre
                votos_mas_altos = cantidad_de_votos

            if cantidad_de_votos < votos_menos_altos:
                edad_candidatos_menos_votos = edad
                nombre_candidato_menos_votos = nombre
                votos_menos_altos = cantidad_de_votos

            suma_edades += edad
            total_candidatos += 1
            votos_totales += cantidad_de_votos

        
        if promedio < 0:
            promedio = suma_edades / total_candidatos

        mensaje = "El candidato con mas votos es {0}\nEl candidato con menos votos es:{1}, con {2} años\nEl promedio de edades de los candidatos es de {3}\nEl total de votos es de {4}".format(nombre_candidato_mas_votos,nombre_candidato_menos_votos,edad_candidatos_menos_votos,promedio,votos_totales)

        alert(title="Candidatos", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
