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
        contador_postulante_Ssr = 0
        bandera_menor_edad = False
        nombre_menor_Edad_jr = ""
        edad_menor_Edad_jr = 0
        contador_f = 0
        acumulador_f = 0
        contador_m = 0
        acumulador_m = 0
        contador_nb = 0
        acumulador_nb = 0
        contador_python = 0
        contador_js = 0
        contador_asp_net = 0

        for postulantes in range(3):
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre:")
            while nombre is None or nombre.isdigit():
                nombre = prompt(title="ERROR", prompt="ERROR,Ingrese su nombre:")
            edad =int(prompt(title="Edad", prompt="Ingrese su edad:"))
            while edad < 18:
                edad =int(prompt(title="ERROR", prompt="ERROR, Ingrese su edad:"))
            genero = prompt(title="Genero", prompt="Ingrese su genero (F, M, NB):")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt(title="EROR", prompt="ERROR, Ingrese su genero (F, M, NB):")
            tecnologia = prompt(title="Tecnologia", prompt="Ingrese su tecnologia (PYTHON - JS - ASP.NET):")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt(title="ERROR", prompt="ERROR,Ingrese su tecnologia (PYTHON - JS - ASP.NET):")
            puesto = prompt(title="Puesto", prompt="Ingrese su puesto (Jr - Ssr - Sr):")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt(title="ERROR", prompt="ERROR, Ingrese su puesto (Jr - Ssr - Sr):")
            
            #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr. 
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad > 25 or edad < 40) and puesto == "Ssr":
                contador_postulante_Ssr += 1
                
            #b. Nombre del postulante Jr con menor edad.
            if puesto == "Jr":
                if bandera_menor_edad == True:
                    nombre_menor_Edad_jr = nombre
                    edad_menor_Edad_jr = edad
                    bandera_menor_edad == False
                else:
                    if edad_menor_Edad_jr > edad:
                        nombre_menor_Edad_jr = nombre
                        edad_menor_Edad_jr = edad

            if puesto == "Jr" and (bandera_menor_edad is True or edad < edad_menor_Edad_jr):
                nombre_menor_Edad_jr = nombre
                edad_menor_Edad_jr = edad
            
            #c. Promedio de edades por género.
            if genero == "F":
                contador_f += 1
                acumulador_f += edad
            if genero == "M":
                contador_m += 1
                acumulador_m += edad
            if genero == "NB":
                contador_nb += 1
                acumulador_nb += edad

            #d. Tecnologia con mas postulantes (solo hay una).
            if tecnologia == "PYTHON":
                contador_python += 1
            elif tecnologia == "JS":
                contador_js += 1
            else:
                contador_asp_net += 1

            if contador_python > contador_js and contador_python > contador_asp_net:
                tecnologia_mas_postulantes = "PYTHON"
            elif contador_js > contador_python and contador_js > contador_asp_net:
                tecnologia_mas_postulantes = "JS"
            else:
                tecnologia_mas_postulantes = "ASP.NET"


        promedio_f = acumulador_f / contador_f
        promedio_m = acumulador_m / contador_m
        promedio_nb = acumulador_nb / contador_nb

        #e. Porcentaje de postulantes de cada genero.
        porcentaje_f = (contador_f/3)*100
        porcentaje_m = (contador_m/3)*100
        porcentaje_nb = (contador_nb/3)*100

        mensaje = "Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {0}\nNombre del postulante Jr con menor edad: {1} y su edad es {2}\nPromedio de edades por género:\nF: {3}\nM: {4}\nNB:{5}\nTecnologia con mas postulantes{4}\nPorcentaje de postulantes de cada gener:\nF: {5}\nM: {6}\nNB:{7}".format(contador_postulante_Ssr,nombre_menor_Edad_jr,edad_menor_Edad_jr,promedio_f,promedio_m,promedio_nb,tecnologia_mas_postulantes,porcentaje_f,porcentaje_m,porcentaje_nb)
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
