'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        contador_a = 0
        nombre_jr_nombre_edad = ""
        edad_jr_menor = float('inf')
        total_edades_f = 0
        total_edades_m = 0
        total_edades_nb = 0
        contador_f = 0
        contador_m = 0
        contador_nb = 0
        contador_python = 0
        contador_js = 0
        contador_aspnet = 0

        for i in range (4):
            alert(title="Postulante", message="Ingrese los datos de los postulante")
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre:")
            edad = prompt(title="Edad", prompt="Ingrese su edad:")
            genero = prompt(title="genero", prompt="Ingrese su genero:")
            tegnologia = prompt(title="tengonolgia", prompt="Ingrese su tegnologia:")
            puesto = prompt(title="puesto", prompt="Ingrese su puesto:")

        if genero == "NB" and tegnologia == "ASP.NET" or tegnologia == "JS" and edad >= 25 and edad <=40 and puesto =="Ssr":
            contador_a += 1

        if puesto == "Jr" and edad < edad_jr_menor:
            nombre_jr_menor_edad = nombre
            edad_jr_menor = edad

        if genero == "F":
            contador_f +=1
            total_edades_f += 1
        elif genero == "M":
            contador_m +=1
            total_edades_m += 1
        else:
            contador_nb +=1
            total_edades_nb += 1

        if tegnologia == "PYTHON":
            contador_python += 1
        elif tegnologia == "JS":
            contador_js += 1
        else:
            contador_aspnet +=1

        promedio_edad_f = total_edades_f / contador_f
        promedio_edad_m = total_edades_m / contador_m
        promedio_edad_nb = total_edades_nb / contador_nb

        porcentaje_f = (contador_f /10)*100
        porcentaje_m = (contador_m /10)*100
        porcentaje_nb = (contador_nb /10)*100
            
        alert(title="Postulantes" "Resultado\nLa cantidad de postulantes NB que programan en ASP.NET o js, tiene entre 25 y 40 y se postula para Ssr {0}\n Nombre del postulante Jr con menor edad: {1}\nPromedio de edades de genero Femenino {2}, masculino {3} y no binario {4}\nLa tegnologia con mas postulantes {5}\n Porcentaje de postulantes de cada genero, Femenino: {6}, masculino: {7} y no binario {8}").format(contador_nb,nombre_jr_menor_edad, promedio_edad_f, promedio_edad_m, promedio_edad_nb, tegnologia, porcentaje_f, porcentaje_m, porcentaje_nb)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
