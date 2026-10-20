"""
Nombre del estudiante: Sarah Melissa Carrejo Gaitán
Grupo: 213022A_2204
Programa: Ingeniería en IA y ciencias de datos
Código fuente: autoría propia

Fase 3 - Arreglos y matrices
Problema 10: Análisis de productividad de 4 empleados durante 3 días.
"""

import tkinter as tk
from tkinter import messagebox

# Constantes: dimensiones de las matrices.
NUMERO_EMPLEADOS = 4
NUMERO_DIAS = 3

# Matrices que se utilizarán en el programa.
matriz_a = []
matriz_b = []
matriz_c = []
# Lista que guardará las cajas de texto de la Matriz A.
entradas_a = []
# Lista que guardará las cajas de texto de la Matriz B.
entradas_b = []
# Lista que guardará las etiquetas de resultado de la Matriz C.
etiquetas_c = []
# Listas con las etiquetas de totales de la Matriz C.
etiquetas_total_empleado = []
etiquetas_total_dia = []
# Colores de la interfaz.
AZUL_OSCURO = "#123B52"
AZUL_MEDIO = "#0E7490"
TURQUESA = "#14B8A6"
NARANJA = "#F59E0B"
ROJO = "#DC2626"
FONDO = "#EAF6FB"
BLANCO = "#FFFFFF"
TEXTO = "#183B4E"

def calcular_productividad():
    # Permite modificar las matrices creadas al inicio del programa.
    global matriz_a, matriz_b, matriz_c

    # Vaciar las matrices antes de calcular nuevamente.
    matriz_a = []
    matriz_b = []
    matriz_c = []

    # Leer y validar la Matriz A.
    for empleado in range(NUMERO_EMPLEADOS):
        fila_a = []

        for dia in range(NUMERO_DIAS):
            texto_tareas = entradas_a[empleado][dia].get().strip()

            try:
                tareas = int(texto_tareas)

            except ValueError:
                messagebox.showerror(
                    "Dato no válido",
                    f"Ingrese un entero mayor que cero en Matriz A, "
                    f"Empleado {empleado + 1}, Día {dia + 1}."
                )
                entradas_a[empleado][dia].focus_set()
                return

            if tareas <= 0:
                messagebox.showerror(
                    "Dato no válido",
                    f"Ingrese un entero mayor que cero en Matriz A, "
                    f"Empleado {empleado + 1}, Día {dia + 1}."
                )
                entradas_a[empleado][dia].focus_set()
                return

            fila_a.append(tareas)

        matriz_a.append(fila_a)

    # Leer y validar la Matriz B.
    for empleado in range(NUMERO_EMPLEADOS):
        fila_b = []

        for dia in range(NUMERO_DIAS):
            texto_minutos = entradas_b[empleado][dia].get().strip()

            try:
                minutos = int(texto_minutos)

            except ValueError:
                messagebox.showerror(
                    "Dato no válido",
                    f"Ingrese un entero mayor que cero en Matriz B, "
                    f"Empleado {empleado + 1}, Día {dia + 1}."
                )
                entradas_b[empleado][dia].focus_set()
                return

            if minutos <= 0:
                messagebox.showerror(
                    "Dato no válido",
                    f"Ingrese un entero mayor que cero en Matriz B, "
                    f"Empleado {empleado + 1}, Día {dia + 1}."
                )
                entradas_b[empleado][dia].focus_set()
                return

            fila_b.append(minutos)

        matriz_b.append(fila_b)

    # Construir Matriz C: Cij = Aij × Bij.
    for empleado in range(NUMERO_EMPLEADOS):
        fila_c = []

        for dia in range(NUMERO_DIAS):
            tiempo_total = matriz_a[empleado][dia] * matriz_b[empleado][dia]
            fila_c.append(tiempo_total)

        matriz_c.append(fila_c)
 # Mostrar la Matriz C en pantalla.
    for empleado in range(NUMERO_EMPLEADOS):
        for dia in range(NUMERO_DIAS):
            etiquetas_c[empleado][dia].config(text=str(matriz_c[empleado][dia]))

        # R3: total por empleado (suma de cada fila).
    totales_empleado = []

    for empleado in range(NUMERO_EMPLEADOS):
        suma_fila = 0

        for dia in range(NUMERO_DIAS):
            suma_fila += matriz_c[empleado][dia]

        totales_empleado.append(suma_fila)
        etiquetas_total_empleado[empleado].config(text=str(suma_fila))

    # Buscar el empleado con el mayor total.
    indice_mejor_empleado = 0

    for empleado in range(1, NUMERO_EMPLEADOS):
        if totales_empleado[empleado] > totales_empleado[indice_mejor_empleado]:
            indice_mejor_empleado = empleado

    # R4: total por día (suma de cada columna).
    totales_dia = []

    for dia in range(NUMERO_DIAS):
        suma_columna = 0

        for empleado in range(NUMERO_EMPLEADOS):
            suma_columna += matriz_c[empleado][dia]

        totales_dia.append(suma_columna)
        etiquetas_total_dia[dia].config(text=str(suma_columna))

    # Buscar el día con el mayor total.
    indice_mejor_dia = 0

    for dia in range(1, NUMERO_DIAS):
        if totales_dia[dia] > totales_dia[indice_mejor_dia]:
            indice_mejor_dia = dia

    # R5: informe consolidado en pantalla.
    etiqueta_mejor_empleado.config(
        text=f"Empleado con mayor tiempo acumulado: Empleado "
             f"{indice_mejor_empleado + 1} "
             f"({totales_empleado[indice_mejor_empleado]} minutos)"
    )
    etiqueta_mejor_dia.config(
        text=f"Día con mayor tiempo total de trabajo: Día "
             f"{indice_mejor_dia + 1} "
             f"({totales_dia[indice_mejor_dia]} minutos)"
    )

    # R5: informe en consola (Terminal de Visual Studio).
    print("Matriz C:")
    for fila in matriz_c:
        print(fila)
    print("Totales por empleado:", totales_empleado)
    print("Totales por día:", totales_dia)
    print("Mayor empleado: Empleado", indice_mejor_empleado + 1)
    print("Mayor día: Día", indice_mejor_dia + 1)
    messagebox.showinfo(
        "Cálculo exitoso",
        "Los datos fueron validados y la Matriz C fue calculada."
    )
# Crear la ventana principal.
ventana = tk.Tk()
ventana.title("Análisis de productividad")
ventana.geometry("980x700")
ventana.resizable(True, True)
ventana.minsize(800, 500)
ventana.configure(bg=FONDO)

# Encabezado.
encabezado = tk.Frame(ventana, bg=AZUL_OSCURO, padx=25, pady=20)
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="ANÁLISIS DE PRODUCTIVIDAD",
    font=("Segoe UI", 20, "bold"),
    fg=BLANCO,
    bg=AZUL_OSCURO
).pack()

tk.Label(
    encabezado,
    text="Registro de tareas y tiempo de 4 empleados durante 3 días",
    font=("Segoe UI", 10),
    fg="#BAE6FD",
    bg=AZUL_OSCURO
).pack(pady=(4, 0))

# Zona desplazable (permite ver todo el contenido en cualquier pantalla).
zona = tk.Frame(ventana, bg=FONDO)
zona.pack(fill="both", expand=True)

lienzo = tk.Canvas(zona, bg=FONDO, highlightthickness=0)
barra = tk.Scrollbar(zona, orient="vertical", command=lienzo.yview)
lienzo.configure(yscrollcommand=barra.set)

barra.pack(side="right", fill="y")
lienzo.pack(side="left", fill="both", expand=True)

# Contenedor principal (ahora vive dentro del lienzo).
contenido = tk.Frame(lienzo, bg=FONDO, padx=35, pady=12)
id_contenido = lienzo.create_window((0, 0), window=contenido, anchor="nw")

def ajustar_region(evento):
    # Actualiza el área que se puede desplazar.
    lienzo.configure(scrollregion=lienzo.bbox("all"))

def ajustar_ancho(evento):
    # Hace que el contenido ocupe todo el ancho de la ventana.
    lienzo.itemconfig(id_contenido, width=evento.width)

def rueda_mouse(evento):
    # Desplaza con la rueda del mouse.
    lienzo.yview_scroll(int(-1 * (evento.delta / 120)), "units")

contenido.bind("<Configure>", ajustar_region)
lienzo.bind("<Configure>", ajustar_ancho)
lienzo.bind_all("<MouseWheel>", rueda_mouse)

# Tarjeta de introducción.
tarjeta_inicio = tk.Frame(contenido, bg=BLANCO, padx=25, pady=20)
tarjeta_inicio.pack(fill="x")

tk.Label(
    tarjeta_inicio,
    text="Datos que se deben registrar",
    font=("Segoe UI", 14, "bold"),
    fg=TEXTO,
    bg=BLANCO
).pack(anchor="w")

tk.Label(
    tarjeta_inicio,
    text=(
        "Matriz A: tareas completadas por cada empleado y día.\n"
        "Matriz B: tiempo promedio por tarea en minutos.\n"
        "Cada valor debe ser un número entero mayor que cero."
    ),
    font=("Segoe UI", 11),
    fg=TEXTO,
    bg=BLANCO,
    justify="left"
).pack(anchor="w", pady=(8, 0))
# Contenedor donde estarán las tarjetas de las matrices.
marco_matrices = tk.Frame(contenido, bg=FONDO)
marco_matrices.pack(fill="x", pady=(20, 0))

# Tarjeta de la Matriz A.
tarjeta_a = tk.Frame(
    marco_matrices,
    bg=BLANCO,
    padx=18,
    pady=18
)
tarjeta_a.pack(side="left", fill="both", expand=True, padx=(0, 8))

tk.Label(
    tarjeta_a,
    text="MATRIZ A - Tareas completadas",
    font=("Segoe UI", 12, "bold"),
    fg=AZUL_MEDIO,
    bg=BLANCO
).pack()

tk.Label(
    tarjeta_a,
    text="Ingrese valores enteros mayores que cero.",
    font=("Segoe UI", 9),
    fg=TEXTO,
    bg=BLANCO
).pack(pady=(3, 10))

# Tabla interna de la Matriz A.
tabla_a = tk.Frame(tarjeta_a, bg=BLANCO)
tabla_a.pack()

tk.Label(
    tabla_a,
    text="Empleado / Día",
    font=("Segoe UI", 9, "bold"),
    fg=BLANCO,
    bg=AZUL_MEDIO,
    padx=8,
    pady=7
).grid(row=0, column=0, padx=1, pady=1)

# Encabezados Día 1, Día 2 y Día 3.
for dia in range(NUMERO_DIAS):
    tk.Label(
        tabla_a,
        text=f"Día {dia + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=AZUL_MEDIO,
        width=8,
        pady=7
    ).grid(row=0, column=dia + 1, padx=1, pady=1)

# Filas de Empleado 1 a Empleado 4 y sus campos de entrada.
for empleado in range(NUMERO_EMPLEADOS):
    tk.Label(
        tabla_a,
        text=f"Empleado {empleado + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg="#DCEFF5",
        width=13,
        pady=7
    ).grid(row=empleado + 1, column=0, padx=1, pady=1)

    fila_entradas = []

    for dia in range(NUMERO_DIAS):
        entrada = tk.Entry(
            tabla_a,
            width=10,
            font=("Segoe UI", 10),
            justify="center",
            relief="solid",
            bd=1
        )
        entrada.grid(row=empleado + 1, column=dia + 1, padx=1, pady=1)
        fila_entradas.append(entrada)

    entradas_a.append(fila_entradas)
    # Tarjeta de la Matriz B.
tarjeta_b = tk.Frame(
    marco_matrices,
    bg=BLANCO,
    padx=18,
    pady=18
)
tarjeta_b.pack(side="left", fill="both", expand=True, padx=(8, 0))

tk.Label(
    tarjeta_b,
    text="MATRIZ B - Minutos por tarea",
    font=("Segoe UI", 12, "bold"),
    fg=TURQUESA,
    bg=BLANCO
).pack()

tk.Label(
    tarjeta_b,
    text="Ingrese valores enteros mayores que cero.",
    font=("Segoe UI", 9),
    fg=TEXTO,
    bg=BLANCO
).pack(pady=(3, 10))

# Tabla interna de la Matriz B.
tabla_b = tk.Frame(tarjeta_b, bg=BLANCO)
tabla_b.pack()

tk.Label(
    tabla_b,
    text="Empleado / Día",
    font=("Segoe UI", 9, "bold"),
    fg=BLANCO,
    bg=TURQUESA,
    padx=8,
    pady=7
).grid(row=0, column=0, padx=1, pady=1)

# Encabezados Día 1, Día 2 y Día 3.
for dia in range(NUMERO_DIAS):
    tk.Label(
        tabla_b,
        text=f"Día {dia + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=TURQUESA,
        width=8,
        pady=7
    ).grid(row=0, column=dia + 1, padx=1, pady=1)

# Filas de Empleado 1 a Empleado 4 y sus campos de entrada.
for empleado in range(NUMERO_EMPLEADOS):
    tk.Label(
        tabla_b,
        text=f"Empleado {empleado + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg="#CCFBF1",
        width=13,
        pady=7
    ).grid(row=empleado + 1, column=0, padx=1, pady=1)

    fila_entradas = []

    for dia in range(NUMERO_DIAS):
        entrada = tk.Entry(
            tabla_b,
            width=10,
            font=("Segoe UI", 10),
            justify="center",
            relief="solid",
            bd=1
        )
        entrada.grid(row=empleado + 1, column=dia + 1, padx=1, pady=1)
        fila_entradas.append(entrada)

    entradas_b.append(fila_entradas)
tk.Button(
    contenido,
    text="Calcular productividad",
    command=calcular_productividad,
    font=("Segoe UI", 12, "bold"),
    bg=NARANJA,
    fg=BLANCO,
    activebackground="#D97706",
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2",
    padx=22,
    pady=11
).pack(pady=(22, 0))
 # Tarjeta de la Matriz C (resultado).
tarjeta_c = tk.Frame(contenido, bg=BLANCO, padx=18, pady=14)
tarjeta_c.pack(fill="x", pady=(12, 0))

tk.Label(
    tarjeta_c,
    text="MATRIZ C - Tiempo total (minutos)",
    font=("Segoe UI", 12, "bold"),
    fg=NARANJA,
    bg=BLANCO
).pack()

# Tabla interna de la Matriz C.
tabla_c = tk.Frame(tarjeta_c, bg=BLANCO)
tabla_c.pack(pady=(8, 0))

tk.Label(
    tabla_c,
    text="Empleado / Día",
    font=("Segoe UI", 9, "bold"),
    fg=BLANCO,
    bg=NARANJA,
    padx=8,
    pady=7
).grid(row=0, column=0, padx=1, pady=1)

# Encabezados Día 1, Día 2 y Día 3.
for dia in range(NUMERO_DIAS):
    tk.Label(
        tabla_c,
        text=f"Día {dia + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=NARANJA,
        width=10,
        pady=7
    ).grid(row=0, column=dia + 1, padx=1, pady=1)

# Encabezado de la columna de totales por empleado.
tk.Label(
    tabla_c,
    text="Total empleado",
    font=("Segoe UI", 9, "bold"),
    fg=BLANCO,
    bg=AZUL_OSCURO,
    width=14,
    pady=7
).grid(row=0, column=NUMERO_DIAS + 1, padx=1, pady=1)

# Filas de empleados con etiquetas vacías que se llenan al calcular.
for empleado in range(NUMERO_EMPLEADOS):
    tk.Label(
        tabla_c,
        text=f"Empleado {empleado + 1}",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg="#FEF3C7",
        width=13,
        pady=7
    ).grid(row=empleado + 1, column=0, padx=1, pady=1)

    fila_etiquetas = []

    for dia in range(NUMERO_DIAS):
        etiqueta = tk.Label(
            tabla_c,
            text="-",
            font=("Segoe UI", 10, "bold"),
            fg=TEXTO,
            bg="#FFFBEB",
            width=10,
            pady=7
        )
        etiqueta.grid(row=empleado + 1, column=dia + 1, padx=1, pady=1)
        fila_etiquetas.append(etiqueta)

    etiquetas_c.append(fila_etiquetas)

    # Total acumulado de este empleado (suma de la fila).
    etiqueta_total = tk.Label(
        tabla_c,
        text="-",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg="#FDE68A",
        width=14,
        pady=7
    )
    etiqueta_total.grid(row=empleado + 1, column=NUMERO_DIAS + 1, padx=1, pady=1)
    etiquetas_total_empleado.append(etiqueta_total)

# Fila de totales por día (suma de cada columna).
tk.Label(
    tabla_c,
    text="Total día",
    font=("Segoe UI", 9, "bold"),
    fg=BLANCO,
    bg=AZUL_OSCURO,
    width=13,
    pady=7
).grid(row=NUMERO_EMPLEADOS + 1, column=0, padx=1, pady=1)

for dia in range(NUMERO_DIAS):
    etiqueta_total = tk.Label(
        tabla_c,
        text="-",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg="#FDE68A",
        width=10,
        pady=7
    )
    etiqueta_total.grid(row=NUMERO_EMPLEADOS + 1, column=dia + 1, padx=1, pady=1)
    etiquetas_total_dia.append(etiqueta_total)

# Tarjeta del informe consolidado (R5).
tarjeta_informe = tk.Frame(contenido, bg=BLANCO, padx=18, pady=14)
tarjeta_informe.pack(fill="x", pady=(12, 18))

tk.Label(
    tarjeta_informe,
    text="INFORME CONSOLIDADO",
    font=("Segoe UI", 12, "bold"),
    fg=AZUL_MEDIO,
    bg=BLANCO
).pack()

etiqueta_mejor_empleado = tk.Label(
    tarjeta_informe,
    text="Empleado con mayor tiempo acumulado: -",
    font=("Segoe UI", 11),
    fg=TEXTO,
    bg=BLANCO
)
etiqueta_mejor_empleado.pack(pady=(8, 0))

etiqueta_mejor_dia = tk.Label(
    tarjeta_informe,
    text="Día con mayor tiempo total de trabajo: -",
    font=("Segoe UI", 11),
    fg=TEXTO,
    bg=BLANCO
)
etiqueta_mejor_dia.pack(pady=(4, 0))
# Esta línea mantiene la ventana abierta.
ventana.mainloop()
