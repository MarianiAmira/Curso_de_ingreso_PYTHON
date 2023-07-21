import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Amira
apellido: Mariani
---
Ejercicio: while_validacion_05
---
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido_Ingresado = self.txt_apellido.get()
        while apellido_Ingresado == "":
            alert(title="Error", message="Ingrese su apellido")
            return False
        while apellido_Ingresado.isdigit():
            alert(title="Error", message="Ingrese su apellido,no se permiten numeros")
            return False
        
        edad_ingresada_txt = self.txt_edad.get()
        edad_ingresada_int = int(edad_ingresada_txt)
        while edad_ingresada_int < 18 or edad_ingresada_int > 90:
            alert(title="Error", message="Ingrese su edad(entre 19 y 90)")
            return False
        
        estado_civil = self.combobox_tipo.get()

        legajo_ingresado_txt = self.txt_legajo.get()
        legajo_ingresado_int = int(legajo_ingresado_txt)
        while legajo_ingresado_int < 1000 or legajo_ingresado_int > 9999:
            alert(title="Error", message="Ingrese el legajo de nuevo(de 4 cifras)")
            return False
        
        mensaje = "Los datos ingresados son:\nSu apellido es: {0}\nSu edad es: {1}\nSu estado civil es: {2}\nSu legajo es:{3}".format(apellido_Ingresado,edad_ingresada_int,estado_civil,legajo_ingresado_int)

        alert(title="Datos Ingresados", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
