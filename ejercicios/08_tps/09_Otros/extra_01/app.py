import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Amira Mariani

Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(
            master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20,
                               columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = []
        self.lista_precio_articulo = []
        self.mensaje = []

    def btn_agregar_on_click(self):
        nombres_articulos = self.txt_nombre_articulo.get()
        while nombres_articulos != "TV" and nombres_articulos != "LICUADORA":
            alert(title="ERROR", message="ERROR, debe ingresar TV o LICUADORA")
            return
        self.lista_nombre_articulo.append(nombres_articulos)

        precios_articulos = self.txt_precio_articulo.get()
        while int(precios_articulos) < 200 or int(precios_articulos) > 1000 and  not precios_articulos.isdigit():
            alert(title="ERROR", message="ERROR, debe ingresar un precio entre 200 y 1000")
            return
        self.lista_precio_articulo.append(precios_articulos)

        pregunta = prompt(title="Pregunta", prompt="Desea ingresar otro producto?")

        alert(title="Datos", message="Los datos se guardaron correctamente")

    def btn_mostrar_on_click(self):
        print(f"Los productos ingresados son: {self.lista_nombre_articulo}")
        print(f"Los precios ingresados de los productos son: {self.lista_precio_articulo}")

    def btn_informar_on_click(self):
        precio_mas_caro = 0
        nombre_precio_mas_caro = ""
        precio_mas_barato = 1000
        nombre_precio_mas_barato = ""
        contador_precios = 0
        acumulador_precios = 0
        precio_articulos_mas_caros_que_promedio = 0
        articulos_mas_caros_que_promedio = ""
        precio_articulos_mas_baratos_que_promedio = 1000
        articulos_mas_baratos_que_promedio = ""

        #1- Articulo mas caro
        for i in range(len(self.lista_precio_articulo)):
            if self.lista_precio_articulo[i] > precio_mas_caro:
                precio_mas_caro = self.lista_precio_articulo[i]
                nombre_precio_mas_caro = self.lista_nombre_articulo[i]
        print(f"El nombre del precio mas caro es: {nombre_precio_mas_caro}")

        #2- Articulo mas barato
        for i in range(len(self.lista_precio_articulo)):
            if self.lista_precio_articulo[i] < precio_mas_barato:
                precio_mas_barato = self.lista_precio_articulo[i]
                nombre_precio_mas_barato = self.lista_nombre_articulo[i]
        print(f"El nombre del precio mas barato es: {nombre_precio_mas_barato}")

        #3- Precio promedio
        for i in range(len(self.lista_precio_articulo)):
            if self.lista_precio_articulo[i]:
                contador_precios +=1
                acumulador_precios += self.lista_precio_articulo[i]
        
        promedio_precios = acumulador_precios/contador_precios
        print(f"El promedio de los precios es: {promedio_precios}")

        #4- Articulos que son mas caros que el promedio
        self.articulos_mas_caros_que_promedio = []
        for i in range(len(self.lista_precio_articulo)):
            if self.lista_precio_articulo[i] > promedio_precios:
                precio_articulos_mas_caros_que_promedio = self.lista_precio_articulo[i]
                articulos_mas_caros_que_promedio = self.lista_nombre_articulo[i]
                self.articulos_mas_caros_que_promedio.append(articulos_mas_caros_que_promedio)
        print(f"Los articulos mas caros que el promedio son: {self.articulos_mas_caros_que_promedio}")

        #5- Articulos que son mas baratos que el promedio
        self.articulos_mas_baratos_que_promedio = []
        for i in range(len(self.lista_precio_articulo)):
            if self.lista_precio_articulo[i] < promedio_precios:
                precio_articulos_mas_baratos_que_promedio = self.lista_precio_articulo[i]
                articulos_mas_baratos_que_promedio = self.lista_nombre_articulo[i]
                self.articulos_mas_baratos_que_promedio.append(articulos_mas_baratos_que_promedio)
        print(f"Los articulos mas baratos que el promedio son: {self.articulos_mas_baratos_que_promedio}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
