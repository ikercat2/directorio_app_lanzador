import streamlit as st
from datetime import datetime

# --- Configuración de la página ---
st.set_page_config(page_title="App de Descarga de Directorio", page_icon="📦", layout="centered")

# --- Imagen superior ---
st.image("lupa-belisario.png", width=180)

# --- Título ---
st.title("📦 App de Descarga de Directorio")
st.markdown("Descarga la versión más reciente del directorio de actualización de datos.")

# --- Información del archivo ---
fecha_modificacion = "07/11/2025 14:32"
url_descarga = "https://drive.google.com/uc?export=download&id=1gUxQzFyE9CJ9TuFB-_Yr1rMKnm-RWdz3"

st.markdown(f"**🕒 Fecha de última actualización:** {fecha_modificacion}")
st.divider()

# --- Botón de descarga (estilo personalizado) ---
st.markdown(
    f"""
    <div style="text-align:center; margin-top: 20px;">
        <a href="{url_descarga}" target="_blank">
            <button style="
                background-color:#0b5394;
                color:white;
                padding:14px 28px;
                border:none;
                border-radius:10px;
                font-size:18px;
                font-weight:600;
                cursor:pointer;
                box-shadow:0px 2px 6px rgba(0,0,0,0.2);">
                ⬇️ Descargar Directorio_actualizacion_datos.exe
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><p style='text-align:center;color:gray;'>© Belisario SAS 2025</p>", unsafe_allow_html=True)
