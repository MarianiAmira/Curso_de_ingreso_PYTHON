import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca_ingresada = self.combobox_marca.get()
        cantidad_ingresada_txt = self.combobox_cantidad.get()
        cantidad_ingresada_int = int(cantidad_ingresada_txt)

        precio_lamparas = 800
        precio_final = cantidad_ingresada_int * precio_lamparas
        
        if cantidad_ingresada_int >= 6:
            precio_final = precio_lamparas * (50/100)
        elif cantidad_ingresada_int == 5 and marca_ingresada == "ArgentinaLuz":
            precio_final = precio_lamparas * (60/100)
        elif cantidad_ingresada_int == 5 and marca_ingresada != "ArgentinaLuz":
            precio_final = precio_lamparas * (70/100)
        elif cantidad_ingresada_int == 4 and (marca_ingresada == "ArgentinaLuz" or marca_ingresada =="FelipeLamparas"):
            precio_final = precio_lamparas * (75/100)
        elif cantidad_ingresada_int == 4 and marca_ingresada != "ArgentinaLuz" and marca_ingresada != "FelipeLamparas":
            precio_final = precio_lamparas * (80/100)
        elif cantidad_ingresada_int == 3 and marca_ingresada == "ArgentinaLuz":
            precio_final = precio_lamparas * (85/100)
        elif cantidad_ingresada_int == 3 and marca_ingresada == "FelipeLamparas":
            precio_final = precio_lamparas * (90/100)
        elif cantidad_ingresada_int == 3 and marca_ingresada != "ArgentinaLuz" and marca_ingresada != "FelipeLamparas":
            precio_final = precio_lamparas * (95/100)

        if precio_final > 4000:
            precio_final = precio_lamparas * (95/100)
        
        mensaje = "El precio final es de {0}".format(precio_final)
        alert(title="Precio Final", message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()