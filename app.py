import streamlit as st
import pandas as pd
import math
import random


class MonteCarlo:
    #inicializo los parametros
    def __init__(self, limite_inferior, limite_superior, tamano_muestra, opcion_funcion):
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.tamano_muestra = tamano_muestra
        self.opcion_funcion = opcion_funcion

        self.muestra_x = []
        self.valores_funcion = []
        self.resultado_integral = 0.0

    def funcion(self, x):
        #defino el denominador 
        ex = math.exp(x)
        emx = math.exp(-x)
        denominador = ex + emx

        #opciones de las funciones
        if self.opcion_funcion == 2:
            return 2.0 / denominador
        return 1.0 / denominador

    def ejecutar_simulacion(self):
        self.muestra_x.clear()
        self.valores_funcion.clear()

        filas = []

        ancho = self.limite_superior - self.limite_inferior
        PI = math.acos(-1.0)
        coeficiente = 2.0 / PI #lo que multiplica la funcion es constante

        suma_acumulada = 0.0

        for i in range(self.tamano_muestra):
            #genero la variable aleatoria con distribucion uniforme y los limites de entrada
            x = random.uniform(self.limite_inferior, self.limite_superior)
            fx = self.funcion(x)

            self.muestra_x.append(x)
            self.valores_funcion.append(fx)

            altura = coeficiente * fx                        
            area_i = ancho * altura / self.tamano_muestra 
            suma_acumulada += area_i

            filas.append({
                "iteracion": i + 1,
                "valor_aleatorio": x,
                "altura": altura,
                "area_aportada": area_i,
                "estimacion_acumulada": suma_acumulada
            })

        self.resultado_integral = suma_acumulada
        df = pd.DataFrame(filas)
        return df, self.resultado_integral


# Interfaz

st.set_page_config(page_title="Monte Carlo Integral", layout="wide")
st.title("Simulación de Monte Carlo")

col1, col2, col3 = st.columns(3)

with col1:
    limite_inferior = st.number_input("Límite inferior (a)", value=-1.0, format="%.2f")
with col2:
    limite_superior = st.number_input("Límite superior (b)", value=1.0, format="%.2f")
with col3:
    tamano_muestra = st.number_input(
        "Número de iteraciones (n)", min_value=1, max_value=1000000, value=1000, step=1
    )

opcion_texto = st.selectbox(
    "Selecciona la función f(x) con la que buscas resolver la integral: ∫[a,b]  2/pi * f(x) dx",
    (
        "1) f(x) = 1 / (e^x + e^-x)",
        "2) f(x) = 2 / (e^x + e^-x)",
    )
)
opcion_funcion = 1 if opcion_texto.startswith("1") else 2

if st.button("Ejecutar simulación"):
    if limite_superior <= limite_inferior:
        st.error("El límite superior debe ser mayor que el límite inferior.")
    else:
        mc = MonteCarlo(
            limite_inferior=float(limite_inferior),
            limite_superior=float(limite_superior),
            tamano_muestra=int(tamano_muestra),
            opcion_funcion=opcion_funcion
        )

        tabla, estimacion_final = mc.ejecutar_simulacion()

        st.subheader("Tabla de iteraciones")
        st.dataframe(tabla, use_container_width=True)

        st.subheader("Estimación final de la integral")
        st.metric(
            label="Valor aproximado",
            value=f"{estimacion_final:.6f}"
        )
