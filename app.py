import streamlit as st
import pandas as pd
import math

import montecarlo.cpp 

st.set_page_config(page_title="Monte Carlo C++", layout="wide")
st.title("Integral por Monte Carlo usando clases en C++")


col1, col2, col3 = st.columns(3)

with col1:
    limite_inferior = st.number_input(
        "Límite inferior (a)", value=-1.0, format="%.4f"
    )

with col2:
    limite_superior = st.number_input(
        "Límite superior (b)", value=1.0, format="%.4f"
    )

with col3:
    tamano_muestra = st.number_input(
        "Número de iteraciones (n)", min_value=1, max_value=1000000,
        value=1000, step=1
    )

opcion_texto = st.selectbox(
    "Selecciona la función f(x)",
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
        mc = montecarlo_cpp.MonteCarlo()
        mc.set_parametros(
            float(limite_inferior),
            float(limite_superior),
            int(tamano_muestra),
            int(opcion_funcion),
        )

        mc.ejecutar_simulacion()

        xs = mc.get_muestra_x()
        fxs = mc.get_valores_funcion()
        resultado_final = mc.get_resultado_integral()

        ancho = limite_superior - limite_inferior
        factor = 2.0 / math.pi

        alturas = [factor * fx for fx in fxs]
        areas = [ancho * h / tamano_muestra for h in alturas]

        estimacion_acum = []
        s = 0.0
        for a in areas:
            s += a
            estimacion_acum.append(s)

        df = pd.DataFrame({
            "valor_aleatorio": xs,
            "altura": alturas,
            "area": areas,
            "estimacion_acumulada": estimacion_acum
        })

        st.subheader("Tabla de iteraciones")
        st.dataframe(df, use_container_width=True)

        st.subheader("Estimación final de la integral")
        st.metric("Valor aproximado", f"{resultado_final:.6f}")
