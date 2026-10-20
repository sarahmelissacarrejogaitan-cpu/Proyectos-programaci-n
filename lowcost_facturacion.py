"""
Nombre del estudiante: [Sarah Melissa Carrejo Gaitán]
Grupo: [213022A_2204]
Programa: [Ingeniería en IA y ciencias de datos]
Código fuente: autoría propia
"""

import tkinter as tk
from tkinter import messagebox

# Constante: tarifa establecida para cada kWh consumido.
COSTO_KWH = 320.5

# Colores que usaremos en la interfaz.
AZUL_OSCURO = "#083344"
VERDE = "#14B8A6"
FONDO = "#ECFEFF"

# Crear la ventana principal del programa.
ventana = tk.Tk()

# Título mostrado en la parte superior de la ventana.
ventana.title("LowCost - Facturación de energía")

# Tamaño inicial de la ventana: ancho x alto.
ventana.geometry("580x570")

# Color de fondo de la ventana.
ventana.configure(bg=FONDO)
# Esta función se ejecutará cuando el usuario presione el botón.
def calcular_factura():
    # Obtener el texto escrito en la caja de consumo.
    texto_consumo = entrada_consumo.get().strip()

    # Permitir coma o punto para números decimales.
    texto_consumo = texto_consumo.replace(",", ".")

    try:
        # Convertir el texto en un número decimal.
        consumo_kwh = float(texto_consumo)

    except ValueError:
        messagebox.showerror(
            "Dato no válido",
            "Ingrese un valor numérico para el consumo en kWh."
        )
        entrada_consumo.focus_set()
        return

    # Validar que el consumo sea mayor que cero.
    if consumo_kwh <= 0:
        messagebox.showerror(
            "Consumo no válido",
            "El consumo mensual debe ser un número mayor que cero."
        )
        entrada_consumo.focus_set()
        return

    # Calcular el valor base.
    valor_base = consumo_kwh * COSTO_KWH

    # Clasificar el consumo y definir el ajuste.
    if consumo_kwh < 150:
        categoria = "Bajo consumo"
        porcentaje_ajuste = -0.05
        tipo_ajuste = "Descuento aplicado"

    elif consumo_kwh <= 350:
        categoria = "Consumo medio"
        porcentaje_ajuste = 0
        tipo_ajuste = "Sin ajuste"

    else:
        categoria = "Alto consumo"
        porcentaje_ajuste = 0.12
        tipo_ajuste = "Recargo aplicado"

    # Calcular ajuste y total final.
    valor_ajuste = valor_base * porcentaje_ajuste
    total_pagar = valor_base + valor_ajuste
    porcentaje_mostrar = porcentaje_ajuste * 100

    # Mostrar los resultados.
       # Preparar el texto que mostrará el ajuste.
    if porcentaje_mostrar < 0:
        texto_ajuste = f"Descuento aplicado: {abs(porcentaje_mostrar):.0f}%"

    elif porcentaje_mostrar > 0:
        texto_ajuste = f"Recargo aplicado: {porcentaje_mostrar:.0f}%"

    else:
        texto_ajuste = "Ajuste aplicado: 0%"

    # Actualizar el contenido de la etiqueta de resultados.
    etiqueta_resultado.config(
        text=(
            f"Categoría: {categoria}\n\n"
            f"Valor base: ${valor_base:,.2f} COP\n\n"
            f"{texto_ajuste}\n\n"
            f"Total a pagar: ${total_pagar:,.2f} COP"
        )
    )

    # Mostrar el marco de resultados cuando exista una factura calculada.
    marco_resultado.pack(fill="x", padx=30, pady=(18, 20))
def limpiar():
    # Borrar el consumo escrito por el usuario.
    entrada_consumo.delete(0, tk.END)

    # Ocultar el resumen anterior.
    marco_resultado.pack_forget()

    # Vaciar el texto almacenado en el resultado.
    etiqueta_resultado.config(text="")

    # Ubicar nuevamente el cursor en la caja de consumo.
    entrada_consumo.focus_set()
# Encabezado de la aplicación.
encabezado = tk.Frame(ventana, bg=AZUL_OSCURO, padx=30, pady=25)
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="LowCost",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg=AZUL_OSCURO
).pack(anchor="w")

tk.Label(
    encabezado,
    text="Consulta y liquidación de consumo mensual de energía",
    font=("Segoe UI", 11),
    fg="#BDEFF0",
    bg=AZUL_OSCURO
).pack(anchor="w", pady=(3, 0))


# Contenedor principal de los elementos de la ventana.
contenido = tk.Frame(ventana, bg=FONDO)
contenido.pack(fill="both", expand=True)

tk.Label(
    contenido,
    text="Consumo mensual",
    font=("Segoe UI", 14, "bold"),
    fg=AZUL_OSCURO,
    bg=FONDO
).pack(anchor="w", padx=30, pady=(28, 4))

tk.Label(
    contenido,
    text="Ingrese el consumo registrado en kilovatios-hora (kWh).",
    font=("Segoe UI", 10),
    fg="#45646C",
    bg=FONDO
).pack(anchor="w", padx=30)


# Caja de texto para que el usuario escriba el consumo.
entrada_consumo = tk.Entry(
    contenido,
    font=("Segoe UI", 15),
    relief="solid",
    bd=1
)
entrada_consumo.pack(fill="x", padx=30, pady=(12, 18), ipady=9)


# Botón que llamará a la función calcular_factura.
boton_calcular = tk.Button(
    contenido,
    text="Calcular factura",
    command=calcular_factura,
    font=("Segoe UI", 11, "bold"),
    bg=VERDE,
    fg="white",
    activebackground="#0F9488",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=11
)
boton_calcular.pack(anchor="w", padx=30)
boton_limpiar = tk.Button(
    contenido,
    text="Nueva consulta",
    command=limpiar,
    font=("Segoe UI", 10),
    bg="#CFFAFE",
    fg=AZUL_OSCURO,
    activebackground="#A5F3FC",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=9
)
boton_limpiar.pack(anchor="w", padx=30, pady=(8, 0))
# Marco donde aparecerá el resumen de la factura.
marco_resultado = tk.Frame(
    contenido,
    bg="white",
    highlightbackground="#99F6E4",
    highlightthickness=2,
    padx=20,
    pady=17
)

tk.Label(
    marco_resultado,
    text="RESUMEN DE FACTURACIÓN",
    font=("Segoe UI", 10, "bold"),
    fg=AZUL_OSCURO,
    bg="white"
).pack(anchor="w", pady=(0, 10))

# Esta etiqueta cambiará su texto cada vez que se calcule una factura.
etiqueta_resultado = tk.Label(
    marco_resultado,
    text="",
    font=("Segoe UI", 11),
    fg="#12313B",
    bg="white",
    justify="left"
)
etiqueta_resultado.pack(anchor="w")
# Permite calcular también al presionar la tecla Enter.
entrada_consumo.bind("<Return>", lambda evento: calcular_factura())

# Deja el cursor listo para escribir al abrir el programa.
entrada_consumo.focus_set()
# Mantiene la ventana abierta para que el usuario interactúe con ella.
ventana.mainloop()
