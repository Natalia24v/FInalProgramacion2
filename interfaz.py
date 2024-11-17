import tkinter as tk
from tkinter import ttk, messagebox
from vinoteca import Vinoteca
from consultas import ConsultasVinoteca

# Inicializar la Vinoteca
Vinoteca.inicializar()

# Colores personalizados para la interfaz
FONDO_VENTANA = "#000000"
FONDO_RESULTADO = "#252928"
TEXTO = "#ffffff"
TEXTO_INACTIVO = "#575959"
BOTON = "#019181"
BOTON_HOVER = "#fc8674"

#Lista todas las bodegas en la pestaña correspondiente.
def listar_bodegas():
    lista_bodegas.delete(0, tk.END)
    bodegas = ConsultasVinoteca.obtener_bodegas()
    if not bodegas:
        lista_bodegas.insert(tk.END, "No se encontraron bodegas.")
    else:
        for bodega in bodegas:
            lista_bodegas.insert(tk.END, bodega.obtenerNombre())

#Busca un vino por ID y muestra su información en la pestaña de Vinos.
def buscar_vino():
    
    id_vino = entrada_id_vino.get()
    if not id_vino:
        messagebox.showerror("Error", "Debes ingresar un ID de vino.")
        return

    vino = ConsultasVinoteca.buscar_vino_por_id(id_vino)
    lista_vinos.delete(0, tk.END)
    if vino:
        lista_vinos.insert(tk.END, f"ID: {vino.obtenerId()}")
        lista_vinos.insert(tk.END, f"Nombre: {vino.obtenerNombre()}")
        lista_vinos.insert(tk.END, f"Bodega: {vino.obtenerBodega().obtenerNombre()}")
    else:
        lista_vinos.insert(tk.END, "Vino no encontrado.")

#Limpia los campos de entrada y la lista de resultados.
def limpiar():
    entrada_id_vino.delete(0, tk.END)
    lista_bodegas.delete(0, tk.END)
    lista_vinos.delete(0, tk.END)
    lista_cepas.delete(0, tk.END)

#Lista todas las cepas en la pestaña correspondiente.
def listar_cepas():
    lista_cepas.delete(0, tk.END)
    cepas = ConsultasVinoteca.obtener_cepas()
    if not cepas:
        lista_cepas.insert(tk.END, "No se encontraron cepas.")
    else:
        for cepa in cepas:
            lista_cepas.insert(tk.END, cepa.obtenerNombre())

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Vinoteca UNER")
ventana.geometry("500x400")
ventana.configure(bg=FONDO_VENTANA)

#estilos personalizados
style = ttk.Style()
style.theme_use('default')

#Configura el aspecto del control de pestañas.
style.configure('TNotebook', background=FONDO_VENTANA, foreground=TEXTO)
#Configura el aspecto de las pestañas individuales.
style.configure('TNotebook.Tab', background=FONDO_VENTANA, foreground=TEXTO_INACTIVO)
style.map('TNotebook.Tab', background=[('selected', FONDO_RESULTADO)], foreground=[('selected', TEXTO)])

#ConfiguraR el aspecto de los frames,
style.configure('TFrame', background=FONDO_VENTANA)
style.configure('TLabel', background=FONDO_VENTANA, foreground=TEXTO)
style.configure('TButton', background=BOTON, foreground=TEXTO)
style.map('TButton', background=[('active', BOTON_HOVER)])

# Crear el control de pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True)

# Pestaña de Bodegas
frame_bodegas = ttk.Frame(notebook)
notebook.add(frame_bodegas, text="Bodegas")

btn_listar_bodegas = tk.Button(frame_bodegas, text="Listar Bodegas", bg=BOTON, fg=TEXTO, activebackground=BOTON_HOVER, command=listar_bodegas)
btn_listar_bodegas.pack(pady=10)

lista_bodegas = tk.Listbox(frame_bodegas, width=60, height=15, bg=FONDO_RESULTADO, fg=TEXTO, font=("Arial", 10))
lista_bodegas.pack(pady=10)


# Pestaña de Vinos
frame_vinos = ttk.Frame(notebook)
notebook.add(frame_vinos, text="Vinos")

lbl_id_vino = ttk.Label(frame_vinos, text="ID del Vino:")
lbl_id_vino.pack(pady=5)
entrada_id_vino = tk.Entry(frame_vinos, bg=FONDO_RESULTADO, fg=TEXTO)
entrada_id_vino.pack(pady=5)

btn_buscar_vino = tk.Button(frame_vinos, text="Buscar Vino", bg=BOTON, fg=TEXTO, activebackground=BOTON_HOVER, command=buscar_vino)
btn_buscar_vino.pack(pady=10)

btn_limpiar = tk.Button(frame_vinos, text="Listar Cepas", bg=BOTON, fg=TEXTO, activebackground=BOTON_HOVER, command=limpiar)
btn_limpiar.pack(pady=10)

lista_vinos = tk.Listbox(frame_vinos, width=60, height=15, bg=FONDO_RESULTADO, fg=TEXTO, font=("Arial", 10))
lista_vinos.pack(pady=10)


# Pestaña de Cepas
frame_cepas = ttk.Frame(notebook)
notebook.add(frame_cepas, text="Cepas")

btn_listar_cepas = tk.Button(frame_cepas, text="Listar Cepas", bg=BOTON, fg=TEXTO, activebackground=BOTON_HOVER, command=listar_cepas)
btn_listar_cepas.pack(pady=10)

lista_cepas = tk.Listbox(frame_cepas, width=60, height=15, bg=FONDO_RESULTADO, fg=TEXTO, font=("Arial", 10))
lista_cepas.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()