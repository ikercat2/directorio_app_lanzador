import streamlit as st
import os
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="App de Descarga de Directorio", page_icon="📦", layout="centered")

# --- Logo ---
logo_path = "lupa-belisario.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=120)

# --- Título ---
st.title("📦 App de Descarga de Directorio")
st.markdown("Descarga la versión más reciente del ejecutable para actualización de datos.")

# --- Ruta local del archivo (solo visible cuando se suba junto con la app) ---
ruta_exe = "Directorio_actualizacion_datos.exe"

if os.path.exists(ruta_exe):
    fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_exe)).strftime("%d/%m/%Y %H:%M:%S")
    st.markdown(f"**🕒 Fecha de última actualización:** {fecha_modificacion}")

    with open(ruta_exe, "rb") as file:
        st.download_button(
            label="⬇️ Descargar Directorio_actualizacion_datos.exe",
            data=file,
            file_name="Directorio_actualizacion_datos.exe",
            mime="application/octet-stream",
        )
else:
    st.error("❌ No se encontró el archivo ejecutable en el repositorio.")
