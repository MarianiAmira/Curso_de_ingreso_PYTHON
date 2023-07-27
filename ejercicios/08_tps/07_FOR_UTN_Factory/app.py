'''
Amira Mariani

UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Pedir:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS o PYTHON
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Cantidad de postulantes de genero Femenino (F) que programan en ASP.NET o JS 
cuya edad este entre 18 y 63, que se hayan postulado para un puesto Sr.
c. Cantidad de postulantes de genero Masculino (M) que programan en JS o PYTHON
cuya edad este entre 50 y 60, que se hayan postulado para un puesto Jr.
d. Nombre y genero de los postulante Seniors (Sr) con mayor y menor edad.
e. Promedio de edades por Puesto.
f. Genero con mas postulantes (solo hay una).
g. Promedio de postulantes PYTHON de cada genero.

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
        self.lista_nombres = []
        self.lista_edades =[]
        self.lista_generos = []
        self.lista_tecnologia = []
        self.lista_puesto = []

        contador_postulantes_Ssr = 0
        contador_postulantes_f_puesto_sr = 0
        contador_postulantes_m_puesto_jr = 0
        edad_mayor_edad_puesto_sr = 0
        nombre_mayor_edad_puesto_sr = ""
        edad_menor_edad_puesto_sr = float('inf')
        nombre_menor_edad_puesto_sr = ""
        contador_puesto_jr = 0
        acumulador_edades_puesto_jr = 0
        contador_puesto_ssr = 0
        acumulador_edades_puesto_ssr = 0
        contador_puesto_sr = 0
        acumulador_edades_puesto_sr = 0
        contador_f = 0
        contador_m = 0
        contador_nb = 0
        contador_postulantes_python_f = 0
        acumulador_postulantes_python_f = 0
        contador_postulantes_python_m = 0
        acumulador_postulantes_python_m = 0
        contador_postulantes_python_nb = 0
        acumulador_postulantes_python_nb = 0


        for i in range(10):
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre")
            while nombre == "" and nombre.isdigit():
                nombre = prompt(title="ERROR", prompt="ERROR,Ingrese su nombre")
            self.lista_nombres.append(nombre)
            edad = int(prompt(title="Edad", prompt="Ingrese su edad"))
            while edad < 18 and edad != edad.isdigit():
                edad = prompt(title="ERROR", prompt="ERROR, Ingrese su edad")
            self.lista_edades.append(edad)
            genero = prompt(title="Genero", prompt="Ingrese su genero(F,M,NB)")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt(title="ERROR", prompt="ERROR,Ingrese su genero(F,M,NB)")
            self.lista_generos.append(genero)
            tecnologia = prompt(title="Tecnologia", prompt="Ingrese su tecnologia((PYTHON - JS - ASP.NET))")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt(title="ERROR", prompt="ERROR,Ingrese su tecnologia((PYTHON - JS - ASP.NET))")
            self.lista_tecnologia.append(tecnologia)
            puesto = prompt(title="Puesto", prompt="Ingrese su puesto((Jr - Ssr - Sr))")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt(title="ERROR", prompt="ERROR, Ingrese su puesto((Jr - Ssr - Sr))")
            self.lista_puesto.append(puesto)

        #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS o PYTHON cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "NB":
                if self.lista_edades[i] > 24 and self.lista_edades[i] < 41:
                    if self.lista_puesto[i] == "Ssr":
                        contador_postulantes_Ssr += 1
        print(f"Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS o PYTHON cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {contador_postulantes_Ssr}")
        
        #b. Cantidad de postulantes de genero Femenino (F) que programan en ASP.NET o JS cuya edad este entre 18 y 63, que se hayan postulado para un puesto Sr.
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "F":
                if self.lista_tecnologia[i] == "ASP.NET" or self.lista_tecnologia[i] == "JS":
                    if self.lista_edades[i] > 17 and self.lista_edades[i] < 64:
                        if self.lista_puesto[i] == "Sr":
                            contador_postulantes_f_puesto_sr += 1
        print(f"antidad de postulantes de genero Femenino (F) que programan en ASP.NET o JS cuya edad este entre 18 y 63, que se hayan postulado para un puesto Sr: {contador_postulantes_f_puesto_sr}")

        #c. Cantidad de postulantes de genero Masculino (M) que programan en JS o PYTHON cuya edad este entre 50 y 60, que se hayan postulado para un puesto Jr.
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "M":
                if self.lista_tecnologia[i] == "JS" or self.lista_tecnologia[i] == "PYTHON":
                    if self.lista_edades[i] > 49 and self.lista_edades[i] < 61:
                        if self.lista_puesto[i] == "Jr":
                            contador_postulantes_m_puesto_jr += 1
        print(f"Cantidad de postulantes de genero Masculino (M) que programan en JS o PYTHON cuya edad este entre 50 y 60, que se hayan postulado para un puesto Jr: {contador_postulantes_m_puesto_jr}")

        #d. Nombre y genero de los postulante Seniors (Sr) con mayor y menor edad.
        for i in range(len(self.lista_puesto)):
            if self.lista_puesto[i] == "Sr":
                if self.lista_edades[i] > edad_mayor_edad_puesto_sr:
                    edad_mayor_edad_puesto_sr = self.lista_edades[i]
                    nombre_mayor_edad_puesto_sr = self.lista_nombres[i]

                if self.lista_edades[i] < edad_menor_edad_puesto_sr:
                    edad_menor_edad_puesto_sr = self.lista_edades[i]
                    nombre_menor_edad_puesto_sr = self.lista_nombres[i]
        print(f"Nombre del postulante Seniors (Sr) con mayor edad: {nombre_mayor_edad_puesto_sr}\nNombre del postulante Seniors (Sr) con menor edad: {nombre_menor_edad_puesto_sr}")

        #e. Promedio de edades por Puesto.
        for i in range(len(self.lista_puesto)):
            if self.lista_puesto[i] == "Jr":
                contador_puesto_jr += 1
                acumulador_edades_puesto_jr += self.lista_edades[i]
            elif self.lista_puesto[i] == "Ssr":
                contador_puesto_ssr += 1
                acumulador_edades_puesto_ssr += self.lista_edades[i]
            elif self.lista_puesto[i] == "Sr": 
                contador_puesto_sr += 1
                acumulador_edades_puesto_sr += self.lista_edades[i]                                         

        if contador_puesto_jr != 0:
            promedio_jr = acumulador_edades_puesto_jr/contador_puesto_jr
        else:
            promedio_jr = "No hay postulantes en Jr"
        print(f"Promedio de edades en el puesto Jr: {promedio_jr}")

        if contador_puesto_ssr != 0:
            promedio_Ssr = acumulador_edades_puesto_ssr / contador_puesto_ssr
        else:
            promedio_Ssr = "No hay postulantes en Ssr"
        print(f"Promedio de edades en el puesto Ssr: {promedio_Ssr}")
            
        if contador_puesto_sr != 0:
            promedio_Sr = acumulador_edades_puesto_sr / contador_puesto_sr
        else:
            promedio_Sr = "No hay postulantes en Sr"
        print(f"Promedio de edades en el puesto Sr: {promedio_Sr}")

        #f. Genero con mas postulantes (solo hay una).
        for i in range(len(self.lista_generos)):
            if self.lista_generos[i] == "F":
                contador_f += 1
            if self.lista_generos[i] == "M":
                contador_m += 1
            if self.lista_generos[i] == "NB":
                contador_nb += 1

            if contador_f > contador_m and contador_f > contador_m:
                mas_postulantes = "Postulantes F"
            elif contador_m > contador_nb:
                mas_postulantes = "Postulantes M"
            else:
                mas_postulantes = "Postulantes NB"
        print(f"Genero con mas postulantes: {mas_postulantes}")

        #g. Promedio de postulantes PYTHON de cada genero.
        for i in range(len(self.lista_tecnologia)):
            if self.lista_tecnologia[i] == "PYTHON":
                if self.lista_generos[i] == "F":
                    contador_postulantes_python_f += 1
                    acumulador_postulantes_python_f += self.lista_edades[i]
                if self.lista_generos[i] == "M":
                    contador_postulantes_python_m += 1
                    acumulador_postulantes_python_m += self.lista_edades[i]
                if self.lista_generos[i] == "NB":
                    contador_postulantes_python_nb += 1
                    acumulador_postulantes_python_nb += self.lista_edades[i]

        if contador_f != 0:
            promedio_python_f = acumulador_postulantes_python_f / contador_postulantes_python_f
        else:
            promedio_python_f = "No hay postulantes PYTHON de genero F"
        print(f"Promedio de postulantes PYTHON de genero F: {promedio_python_f}")

        if contador_m != 0:
            promedio_python_m = acumulador_postulantes_python_m / contador_postulantes_python_m
        else:
            promedio_python_m = "No hay postulantes PYTHON de genero M"
        print(f"Promedio de postulantes PYTHON de genero M: {promedio_python_m}")

        if contador_nb != 0:
            promedio_python_nb = acumulador_postulantes_python_nb / contador_postulantes_python_nb
        else:
            promedio_python_nb = "No hay postulantes PYTHON de genero NB"
        print(f"Promedio de postulantes PYTHON de genero NB: {promedio_python_nb}")

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
