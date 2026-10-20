"""
Nombre del estudiante: Sarah Melissa Carrejo Gaitán
Grupo: 213022A_2204
Programa: Ingeniería en IA y ciencias de datos
Código fuente: autoría propia

Fase 3 - Estructuras repetitivas
Problema 1: Monitoreo de temperatura de un horno industrial.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Constantes del rango operativo.
TEMPERATURA_MINIMA = 180
TEMPERATURA_MAXIMA = 200

# Paleta de colores.
AZUL_OSCURO = "#123B52"
AZUL_FRIO = "#0EA5E9"
VERDE_OPTIMO = "#10B981"
NARANJA_PRECAUCION = "#F59E0B"
ROJO_ALERTA = "#DC2626"
FONDO = "#EAF6FB"
BLANCO = "#FFFFFF"
TEXTO = "#183B4E"
GRIS_TERMOMETRO = "#CBD5E1"


def dibujar_termometro(temperatura=None, color_termometro=GRIS_TERMOMETRO):
    """Dibuja o actualiza el termómetro en el lienzo."""

    lienzo.delete("all")

    # Contorno del termómetro.
    lienzo.create_rectangle(
        128, 35, 192, 240,
        outline=AZUL_OSCURO,
        width=4
    )

    # Fondo de la columna.
    lienzo.create_rectangle(
        142, 65, 178, 240,
        fill=GRIS_TERMOMETRO,
        outline=""
    )

    # Si existe una temperatura, calcular la altura visual del líquido.
    if temperatura is not None:
        temperatura_visual = max(150, min(temperatura, 230))
        nivel = int((temperatura_visual - 150) / 80 * 170)
        posicion_superior = 230 - nivel

        lienzo.create_rectangle(
            142, posicion_superior, 178, 240,
            fill=color_termometro,
            outline=""
        )

    # Base circular del termómetro.
    lienzo.create_oval(
        100, 205, 220, 325,
        fill=color_termometro,
        outline=AZUL_OSCURO,
        width=4
    )

    # Marcas de referencia.
    lienzo.create_text(
        260, 60,
        text="200 °C",
        font=("Segoe UI", 10),
        fill=ROJO_ALERTA
    )

    lienzo.create_text(
        260, 145,
        text="190 °C",
        font=("Segoe UI", 10),
        fill=TEXTO
    )

    lienzo.create_text(
        260, 225,
        text="180 °C",
        font=("Segoe UI", 10),
        fill=AZUL_FRIO
    )

    # Mostrar el valor numérico solo después de ingresar una temperatura.
    if temperatura is not None:
        lienzo.create_text(
            160, 18,
            text=f"{temperatura} °C",
            font=("Segoe UI", 13, "bold"),
            fill=color_termometro
        )


def monitorear_temperatura():
    """Valida, clasifica y muestra la temperatura ingresada."""

    texto_temperatura = entrada_temperatura.get().strip()

    try:
        temperatura = int(texto_temperatura)

    except ValueError:
        messagebox.showerror(
            "Dato no válido",
            "Ingrese una temperatura entera válida."
        )
        entrada_temperatura.focus_set()
        return

    # Estado general y Alerta requerida.
    if temperatura > TEMPERATURA_MAXIMA:
        mensaje = (
            "Estado: temperatura alta\n"
            "Alerta: enfriamiento"
        )
        color_estado = ROJO_ALERTA

    elif temperatura < TEMPERATURA_MINIMA:
        mensaje = (
            "Estado: temperatura baja\n"
            "Alerta: calentamiento"
        )
        color_estado = AZUL_FRIO

    else:
        mensaje = (
            "Estado: temperatura optima\n"
        )
        color_estado = VERDE_OPTIMO

    # Color del termómetro según la cercanía a los límites.
    if temperatura < 185:
        color_termometro = AZUL_FRIO

    elif temperatura <= 195:
        color_termometro = VERDE_OPTIMO

    elif temperatura <= TEMPERATURA_MAXIMA:
        color_termometro = NARANJA_PRECAUCION

    else:
        color_termometro = ROJO_ALERTA

    etiqueta_estado.config(
        text=f"{mensaje}\nLectura actual: {temperatura} °C",
        fg=color_estado
    )

    dibujar_termometro(temperatura, color_termometro)




    # Mostrar el resultado en pantalla antes de preguntar.
    ventana.update()
    preguntar_continuar()
    
def finalizar_monitoreo():
    """Bloquea la interfaz cuando el usuario decide terminar."""

    entrada_temperatura.config(state="disabled")
    entrada_temperatura.unbind("<Return>")

    for boton in marco_botones.winfo_children():
        boton.config(state="disabled")

    etiqueta_estado.config(
        text=etiqueta_estado.cget("text") + "\n\nMonitoreo finalizado."
    )


def preguntar_continuar():
    """Pregunta si se desea continuar. 1 = sí, 0 = no."""

    while True:
        respuesta = simpledialog.askstring(
            "Continuar",
            "¿Desea continuar? (1: sí, 0: no)",
            parent=ventana
        )

        # Si cierra o cancela el cuadro, se toma como terminar.
        if respuesta is None:
            respuesta = "0"

        respuesta = respuesta.strip()

        if respuesta == "1":
            limpiar_lectura()
            return

        if respuesta == "0":
            finalizar_monitoreo()
            return

        messagebox.showerror(
            "Dato no válido",
            "Ingrese 1 para continuar o 0 para finalizar."
        )

def limpiar_lectura():
    """Prepara la interfaz para registrar otra lectura."""

    entrada_temperatura.delete(0, tk.END)

    etiqueta_estado.config(
        text="Ingrese una temperatura para iniciar el monitoreo.",
        fg=TEXTO
    )

    dibujar_termometro()
    entrada_temperatura.focus_set()


# Ventana principal.
ventana = tk.Tk()
ventana.title("Horno Industrial - Monitoreo de temperatura")
ventana.geometry("620x720")
ventana.resizable(False, False)
ventana.configure(bg=FONDO)

# Encabezado.
encabezado = tk.Frame(ventana, bg=AZUL_OSCURO, padx=25, pady=22)
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="MONITOREO DEL HORNO INDUSTRIAL",
    font=("Segoe UI", 18, "bold"),
    fg=BLANCO,
    bg=AZUL_OSCURO
).pack()

tk.Label(
    encabezado,
    text="Rango operativo: 180 °C a 200 °C",
    font=("Segoe UI", 10),
    fg="#BAE6FD",
    bg=AZUL_OSCURO
).pack(pady=(5, 0))

# Tarjeta principal.
tarjeta = tk.Frame(ventana, bg=BLANCO, padx=25, pady=20)
tarjeta.pack(fill="both", expand=True, padx=35, pady=25)

tk.Label(
    tarjeta,
    text="Estado de la temperatura",
    font=("Segoe UI", 14, "bold"),
    fg=TEXTO,
    bg=BLANCO
).pack()

# Lienzo del termómetro.
lienzo = tk.Canvas(
    tarjeta,
    width=320,
    height=330,
    bg=BLANCO,
    highlightthickness=0
)
lienzo.pack(pady=12)

dibujar_termometro()

# Mensaje de estado.
etiqueta_estado = tk.Label(
    tarjeta,
    text="Ingrese una temperatura para iniciar el monitoreo.",
    font=("Segoe UI", 11),
    fg=TEXTO,
    bg=BLANCO,
    justify="center"
)
etiqueta_estado.pack(pady=(0, 12))

# Entrada de temperatura.
marco_entrada = tk.Frame(tarjeta, bg=BLANCO)
marco_entrada.pack(pady=(5, 12))

tk.Label(
    marco_entrada,
    text="Temperatura del horno:",
    font=("Segoe UI", 11, "bold"),
    fg=TEXTO,
    bg=BLANCO
).pack(side="left", padx=(0, 8))

entrada_temperatura = tk.Entry(
    marco_entrada,
    width=8,
    font=("Segoe UI", 14),
    justify="center",
    relief="solid",
    bd=1
)
entrada_temperatura.pack(side="left")

tk.Label(
    marco_entrada,
    text="°C",
    font=("Segoe UI", 11, "bold"),
    fg=TEXTO,
    bg=BLANCO
).pack(side="left", padx=(8, 0))

# Botones.
marco_botones = tk.Frame(tarjeta, bg=BLANCO)
marco_botones.pack()

tk.Button(
    marco_botones,
    text="Monitorear temperatura",
    command=monitorear_temperatura,
    font=("Segoe UI", 11, "bold"),
    bg=NARANJA_PRECAUCION,
    fg=BLANCO,
    activebackground="#D97706",
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=10
).pack(side="left", padx=5)

tk.Button(
    marco_botones,
    text="Nueva lectura",
    command=limpiar_lectura,
    font=("Segoe UI", 11),
    bg="#DCEFF5",
    fg=AZUL_OSCURO,
    activebackground="#BFDBE5",
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=10
).pack(side="left", padx=5)

# Permitir calcular con la tecla Enter.
entrada_temperatura.bind(
    "<Return>",
    lambda evento: monitorear_temperatura()
)

entrada_temperatura.focus_set()
ventana.mainloop()
