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
        nombre_mas_votos = ""
        votos_mas_altos = -1
        nombre_menos_votos = ""
        edad_menos_votos = -1
        votos_menos_altos = float("inf")
        suma_edades = 0
        total_candidatos = 0
        votos_totales = 0

        candidatos = []
        while True:
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre")
            edad = int(prompt(title="Edad", prompt="Ingrese su edad(mayor a 25)"))
            while edad <=25:
                edad = int(prompt(title="Edad", prompt="Error,Ingrese su edad(mayor a 25)"))

            votos = int(prompt(title="Votos", prompt="Ingrese sus votos(mayor a 0)"))
            while votos < 0:
                votos = int(prompt(title="Votos", prompt="Error,Ingrese sus votos(mayor a 0)"))

            #agregar los datos a la lista
            candidatos.append((nombre,edad,votos))

            pregunta = question(title="Candidatos", message="Quiere agregar otro candidato?")
            if pregunta != True:
                break

        for candidato in candidatos:
            nombre, edad, votos = candidato

            if votos > votos_mas_altos:
                nombre_mas_votos = nombre
                votos_mas_altos = votos

            if votos < votos_menos_altos:
                nombre_menos_votos = nombre
                edad_menos_votos = edad
                votos_menos_altos = votos

            suma_edades += edad
            total_candidatos += 1
            votos_totales += votos
            
        promedio_edades = suma_edades / total_candidatos

        mensaje = "El candidato con mas votos es: {0}\nEl candidato con menos votos es: {1}, con {2} años\nEl promedio de edades de los candidatos es: {3}\nEl total de votos es: {4}".format(nombre_mas_votos, nombre_menos_votos, edad_menos_votos, promedio_edades, votos_totales)

        alert(title="Candidatos", message=mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
