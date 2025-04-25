import pandas as pd #pip install pandas
import streamlit as st #pip install streamlit
import os

# ---------------------- CONFIGURACIÓN ----------------------
st.set_page_config(page_title="Transformadores", layout="wide")

# ---------------------- FUNCIONES --------------------------
def cargar_tabla(nombre_archivo):
    ruta = os.path.join("normas", "tablas", nombre_archivo)
    try:
        return pd.read_csv(ruta, sep=r"\s+", engine="python", decimal=",")

    except Exception as e:
        st.error(f"No se pudo cargar el archivo {nombre_archivo}: {e}")
        return None

def interpolar_valores(tabla, potencia_objetivo):
    tabla_ordenada = tabla.sort_values(by="Potencia")
    potencias = tabla_ordenada["Potencia"].values

    if potencia_objetivo < potencias[0] or potencia_objetivo > potencias[-1]:
        return None

    for i in range(len(potencias) - 1):
        p1, p2 = potencias[i], potencias[i + 1]
        if p1 <= potencia_objetivo <= p2:
            fila1 = tabla_ordenada.iloc[i]
            fila2 = tabla_ordenada.iloc[i + 1]
            interpolado = {}
            for columna in tabla.columns:
                if columna == "Potencia":
                    interpolado[columna] = potencia_objetivo
                else:
                    interpolado[columna] = fila1[columna] + (
                        (potencia_objetivo - p1) / (p2 - p1)
                    ) * (fila2[columna] - fila1[columna])
            return interpolado
    return None

# ---------------------- INTERFAZ ---------------------------
st.title("🔎 Consulta de Pérdidas en Transformadores")
st.markdown("Diseñado en Python por: **Ing. Jose Barreto - V.002**")

# Imagen/logo
if os.path.exists("logo.png"):
    st.image("logo.png", width=150)

# Selección de norma
archivos = {
    "Norma INEN 2115-3F Aceite (<25kV / <1.2kV)": "Norma_inen_2115_3f_Aceite.prn",
    "Norma INEN 2114-1F Aceite (<25kV / <1.2kV)": "Norma_inen_2114_1F_Aceite.prn",
    "Norma NTC 819-3F Aceite (<15kV / <1.2kV)": "Nomra_NTC_819_3F_Aceite.prn",
    "Norma NTC 3445-3F Seco (<1.2kV / <1.2kV)": "Norma_NTC_3445_3f_Seco.prn",
    "Norma NTC 3445-3F Seco (<15kV / <1.2kV)": "Norma_NTC_3445_3f_Seco_AT.prn",
    "Norma RVR-3F Petroleos": "Norma_RVR_3f_Petroleos.prn"
}

norma_seleccionada = st.selectbox("📘 Seleccione una norma:", list(archivos.keys()))
archivo = archivos[norma_seleccionada]

tabla = cargar_tabla(archivo)

if tabla is not None:
    st.subheader("📊 Tabla de Referencia")
    st.dataframe(tabla, use_container_width=True)

    # Ingreso de potencia
    potencia_input = st.text_input("⚡ Ingrese la potencia (kVA):", placeholder="Ej: 150")
    if potencia_input:
        try:
            potencia = float(potencia_input.replace(",", "."))
            resultado = interpolar_valores(tabla, potencia)

            if resultado:
                st.subheader("📌 Resultados Interpolados")
                df_resultado = pd.DataFrame([resultado])
                st.dataframe(df_resultado, use_container_width=True)
            else:
                st.warning("La potencia está fuera del rango de la tabla.")

        except ValueError:
            st.error("⚠️ Ingrese un valor numérico válido.")



# cd "\\urano\Empresa\2025\Dep. de Ingeniería\Dep. Ing Eléctrica\A. de Ing\Proyectos\0. Python\Consultor_tablas_Trafo_web"
# streamlit run app_streamlit.py

#  git add ., git commit -m "Corrijo requirements" y git push
