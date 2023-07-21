import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Piedra, Papel o Tijera (v 1.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió
'''

class App(customtkinter.CTk):
     
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_piedra = customtkinter.CTkButton(master=self, text="Piedra", command=self.btn_piedra_on_click)
        self.btn_piedra.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_papel = customtkinter.CTkButton(master=self, text="Papel", command=self.btn_papel_on_click)
        self.btn_papel.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_tijera = customtkinter.CTkButton(master=self, text="Tijera", command=self.btn_tijera_on_click)
        self.btn_tijera.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_restart = customtkinter.CTkButton(master=self, text="RESTART", command=self.btn_restart_on_click, fg_color="red")
        self.btn_restart.grid(row=5, pady=20, columnspan=2, sticky="nsew")
        
        self.cpu_elije()
        #print(self.seleccion_cpu)

    def deshabilitar_botones(self):
        self.btn_piedra.configure(state="disabled")
        self.btn_papel.configure(state="disabled")
        self.btn_tijera.configure(state="disabled")

    def btn_restart_on_click(self):
        self.btn_piedra.configure(state="normal")
        self.btn_papel.configure(state="normal")
        self.btn_tijera.configure(state="normal")
        self.cpu_elije()
        #print(self.seleccion_cpu)

    def cpu_elije(self):
        import random
        self.seleccion_cpu = random.randint(1, 3)
        if self.seleccion_cpu ==1:
            print("La cpu eligio : Piedra")
        elif self.seleccion_cpu ==2:
            print("La cpu eligio : Papel")
        else:
            print("La cpu eligio : Tijera")
     
    def btn_piedra_on_click(self):
        self.deshabilitar_botones()
        seleccion_jugador = "Piedra"
        if seleccion_jugador == "Piedra":
            if self.seleccion_cpu == 1:
                mensaje = "empate"
            elif self.seleccion_cpu == 2:
                mensaje = "Perdiste"
            else:
                mensaje = "Ganaste"
        alert(title="Resultado", message=mensaje)


    def btn_papel_on_click(self):
        self.deshabilitar_botones()
        seleccion_jugador = "Papel"
        if seleccion_jugador == "Papel":
            if self.seleccion_cpu == 1:
                mensaje = "Ganaste"
            elif self.seleccion_cpu == 2:
                mensaje = "Empate"
            else:
                mensaje = "Perdiste"
        alert(title="Resultado", message=mensaje)

    def btn_tijera_on_click(self):
        self.deshabilitar_botones()
        seleccion_jugador = "Tijera"
        if seleccion_jugador == "Tijera":
            if self.seleccion_cpu == 1:
                mensaje = "Perdiste"
            elif self.seleccion_cpu == 2:
                mensaje = "Ganaste"
            else:
                mensaje = "Empate"
        alert(title="Resultado", message=mensaje)
    

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()