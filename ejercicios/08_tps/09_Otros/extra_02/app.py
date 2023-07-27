import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:

La UTN nos solicita la creación de una aplicación para obtener información 
estadistica de las evaluaciones.

1. Al presionar el botón "Ingresar notas", se deberá solicitar mediante prompt 
las notas del los alumn@s. 

	A - Se deberá repetir la solicitud hasta que el usuario haga clic en el botón  
    "Cancelar" del prompt
	B - Se deberá validar que la nota sea un numero entero entre el 0 y el 10.
	C - Las notas ingresadas se deberán ir guardando en una lista.

2. Al presionar el botón "Mostrar notas" debemos mostrar por la terminal el 
listado de las notas, primero indicando su posición en la lista y luego el 
valor de la nota. Con el siguiente formato:

        "1 - Nota: 8"
        "2 - Nota: 4"
        "3 - Nota: 10"
        ...

3. Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Nota mas baja
	B - Nota mas alta
	C - Promedio de todas las notas
	D - Cantidad de evaluaciones con nota 10
	E - En el caso que el promedio sea menor a 3, informar con la leyenda: "El promedio desaprobo"
	En el caso que el promedio sea mayor a 4: "El promedio aprobo"
	En el caso que el promedio sea mayor a 7: "El promedio promocionó"

	Para el punto E se deberá utilizar match.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_ingresar_notas = customtkinter.CTkButton(master=self, text="Ingresar Notas", command=self.btn_ingresar_notas_on_click)
        self.btn_ingresar_notas.grid(row=3, pady=20, columnspan=2, sticky="news")

        self.btn_mostrar_notas = customtkinter.CTkButton(master=self, text="Mostrar Notas", command=self.btn_mostrar_notas_on_click)
        self.btn_mostrar_notas.grid(row=4, pady=20, columnspan=2, sticky="news")
        
        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, text="Generar Informe de Notas", command=self.btn_generar_informe_notas_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")
        
            
    def btn_ingresar_notas_on_click(self):
        self.notas_ingresadas = []

        respuesta = "Si"
        while respuesta != None:
            nota = prompt(title="Notas", prompt="Ingrese su nota")
            while not nota.isdigit() or int(nota) < 0 or int(nota) > 10:
                nota = prompt(title="ERROR", prompt="ERROR,Ingrese su nota")
            
            respuesta = prompt(title="Pregunta", prompt="Quiere ingresar otra nota?")
            self.notas_ingresadas.append(int(nota))
    
    def btn_generar_informe_notas_on_click(self):
        nota_mas_baja = 10
        nota_mas_alta = 0
        contador_notas = 0
        acumulador_notas = 0
        contador_notas_10 = 0

        #A - Nota mas baja
        for i in range(len(self.notas_ingresadas)):
            if self.notas_ingresadas[i] < nota_mas_baja:
                nota_mas_baja = self.notas_ingresadas[i]
        print(f"La nota mas baja es {nota_mas_baja}")

        #B - Nota mas alta
        for i in range(len(self.notas_ingresadas)):
            if self.notas_ingresadas[i] > nota_mas_alta:
                nota_mas_alta = self.notas_ingresadas[i]
        print(f"La nota mas alta es {nota_mas_alta}")

        #C - Promedio de todas las notas
        for i in range(len(self.notas_ingresadas)):
            contador_notas += 1
            acumulador_notas += self.notas_ingresadas[i]

        promedio_notas = acumulador_notas // contador_notas
        print(f"El promedio de notas es de: {promedio_notas}")
        
        #E - En el caso que el promedio sea menor a 3, informar con la leyenda: "El promedio desaprobo"
        # En el caso que el promedio sea mayor a 4: "El promedio aprobo"
        # En el caso que el promedio sea mayor a 7: "El promedio promocionó"
        match(promedio_notas):
            case 1|2|3:
                mensaje = "El promedio desaprobo"
            case 4|5|6:
                mensaje = "El promedio aprobo"
            case _:
                mensaje = "El promedio promocionó"
        print(mensaje)

        #D - Cantidad de evaluaciones con nota 10
        for i in range(len(self.notas_ingresadas)):
            if self.notas_ingresadas[i] == 10:
                contador_notas_10 += 1
        print(f"La cantidad de notas 10 son: {contador_notas_10}")
        

    def btn_mostrar_notas_on_click(self):
        print("Listado de notas:")
        for i, nota in enumerate(self.notas_ingresadas, start=1):
            print(f"{i} - Nota: {nota}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()  
            