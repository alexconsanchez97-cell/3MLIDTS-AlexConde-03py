from email import message
import tkinter as tk
from tkinter import messagebox
#Ventana
ventana = tk.Tk()
ventana.title("Conversor basico de temperatura")

#Metodos
def Calcular_temps():
    if tbCelsius.get() or tbFarenheit.get() or tbKelvin.get():
        try:
            if (tbCelsius.get()):
                ce = float(tbCelsius.get())
                fa = (ce * 9/5) +32
                ke = ce + 273.15
                tbFarenheit.delete(0, tk.END)
                tbFarenheit.insert(0, str(round(fa, 2)))
                tbKelvin.delete(0, tk.END)
                tbKelvin.insert(0, str(round(ke, 2)))
            elif tbFarenheit.get():
                fa = float(tbFarenheit.get())
                ce = (fa - 32) * 5/9
                ke = ce + 273.15
                tbCelsius.delete(0, tk.END)
                tbCelsius.insert(0, str(round(ce, 2)))
                tbKelvin.delete(0, tk.END)
                tbKelvin.insert(0, str(round(ce, 2)))
            elif tbKelvin.get():
                ke = float(tbKelvin.get())
                ce = ke - 273.15
                fa = (ce * 9/5) + 32
                tbCelsius.delete(0, tk.END)
                tbCelsius.insert(0, str(round(ce, 2)))
                tbFarenheit.delete(0, tk.END)
                tbFarenheit.insert(0, str(round(fa,2)))
        except ValueError:
            messagebox.showinfo("Error", "Ingrese valores validos")
    else:
        messagebox.showinfo("Advertencia", "No se puede dejar en blanco")

def Limpiar():
    tbCelsius.delete(0, tk.END)
    tbFarenheit.delete(0, tk.END)
    tbKelvin.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Se borarron los valores de los campos.")
    messagebox.showinfo(message="Limpiar", title= "Se borraron los valores")

#Etiquetas
#tk.Label(ventana, text = "Celsius:").grid(row=0, column=0,padx=10,pady=10)
lbCelsius = tk.Label(ventana, text= "Celsius :")
lbCelsius.grid(row=0, column= 0,padx=10, pady = 10)
#tk.Label(ventana, text = "Farenheit:").grid(row=1, column=0,padx=10,pady=10)
lbFarenheit = tk.Label(ventana, text = "Farenheit :")
lbFarenheit.grid(row = 1, column= 0, padx= 10, pady = 10)
#tk.Label(ventana, text = "Kelvin:").grid(row=2, column=0,padx=10,pady=10)
lbKelvin = tk.Label(ventana, text = "Kelvin :")
lbKelvin.grid(row = 2, column= 0, padx= 10, pady = 10)

#Entradas
tbCelsius = tk.Entry(ventana)
tbFarenheit = tk.Entry(ventana)
tbKelvin = tk.Entry(ventana)

tbCelsius.grid(row=0, column=1,padx=10,pady=10)
tbFarenheit.grid(row=1, column = 1, padx = 10, pady = 10)
tbKelvin.grid(row=2, column= 1, padx= 10, pady = 10)

#Botones
btnCalcular = tk.Button(ventana, text = "Calcular", command=Calcular_temps)
btnLimpiar = tk.Button(ventana, text = "Limpiar", command=Limpiar)

btnCalcular.grid(row=3, column =0, columnspan= 2, pady = 10)
btnLimpiar.grid(row=4, column= 0, columnspan= 2, pady = 10)
ventana.mainloop()