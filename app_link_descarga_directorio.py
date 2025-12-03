import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="App de Descarga de Directorio",
    page_icon="📦",
    layout="centered"
)

html_page = """
<div style="text-align:center; margin-top:20px;">
    <img src="lupa-belisario.png" width="160">
</div>

<div style="
    background: #ffffff; 
    border-radius: 18px; 
    padding: 40px 35px; 
    box-shadow: 0px 6px 16px rgba(0,0,0,0.12);
    margin-top: 25px;
    font-family: 'Segoe UI', sans-serif;
">

    <h1 style="
        text-align:center; 
        color:#0b5394; 
        font-size:34px;
        margin-bottom:5px;
    ">
        📦 App de Descarga de Directorio
    </h1>

    <p style="
        text-align:center; 
        font-size:18px; 
        color:#555; 
        margin-bottom:10px;
    ">
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

    <div style="text-align:center; margin-top:30px;">
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

</div>

<p style='text-align:center; color:gray; margin-top:25px; font-size:14px;'>
    © Belisario SAS 2025
</p>
"""

components.html(html_page, height=900, scrolling=False)
