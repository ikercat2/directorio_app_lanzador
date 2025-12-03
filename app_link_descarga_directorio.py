import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="App de Descarga de Directorio",
    page_icon="📦",
    layout="centered"
)

# Convertir imágenes a base64
def load_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = load_image_base64("lupa-belisario.png")
fondo_base64 = load_image_base64("manos manitas.jpg")

st.markdown(
    f"""
    <style>
        .stApp {{
            background: url('data:image/jpeg;base64,{fondo_base64}') !important;
            background-size: cover !important;
            background-position: center !important;
            filter: brightness(1.1);
        }}

        /* Capa difuminada encima de toda la app */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            backdrop-filter: blur(8px);
            background: rgba(255,255,255,0.25);
            z-index: -1;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

html_page = f"""
<div style="text-align:center; margin-top:20px;">
    <img src="data:image/png;base64,{logo_base64}" width="500">
</div>

<div style="
    background: rgba(255, 255, 255, 0.85);
    border-radius: 18px;
    padding: 40px 35px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.12);
    margin-top: 25px;
    font-family: 'Segoe UI', sans-serif;
    backdrop-filter: blur(4px);
    display: inline-block;
    width: 80%;
    max-width: 650px;
">

    <h1 style="color:#0b5394; font-size:34px; margin-bottom:5px;">
        📦 App de Descarga de Directorio
    </h1>

    <p style="font-size:18px; color:#555;">
        Descarga la versión más reciente del directorio de actualización de datos.
    </p>

    <div style="
        background:#f0f4f8;
        padding:12px 18px;
        border-radius:10px;
        font-size:17px;
        color:#333;
        margin:22px auto;
        width:85%;
        text-align:center;
        border-left:5px solid #0b5394;
    ">
        🕒 <strong>Última actualización:</strong> 03/11/2025 7:55 AM
    </div>

    <a href="https://drive.google.com/uc?export=download&id=1gUxQzFyE9CJ9TuFB-_Yr1rMKnm-RWdz3" target="_blank">
        <button style="
            background-color:#0b5394;
            color:white;
            padding:16px 36px;
            border:none;
            border-radius:12px;
            font-size:20px;
            font-weight:700;
            cursor:pointer;
            transition:0.25s;
            box-shadow:0px 4px 10px rgba(0,0,0,0.15);
        ">
            ⬇️ Descargar Directorio_actualizacion_datos.exe
        </button>
    </a>

</div>

<p style='color:gray; margin-top:20px; font-size:14px;'>
    © Belisario SAS 2025
</p>
"""

components.html(html_page, height=950, scrolling=False)
