import qrcode
import streamlit as st
from PIL import Image

# Directorio y nombre del archivo QR
filename = "qr_code.png"

# Función para generar el código QR
def generar_qr(url, filename):
    qr = qrcode.qrcode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Configuración de la página de Streamlit
st.set_page_config(page_title="Generador de QR", page_icon="", layout="centered")
st.title("Generador de QR")

# Entrada de URL
url = st.text_input("Introduce la URL")

# Botón para generar el código QR
if st.button("Generar código QR"):
    if url:
        generar_qr(url, filename)
        st.image(filename, use_column_width=True)

        # Abrir y leer el archivo QR generado
        with open(filename, "rb") as f:
            image_data = f.read()
        
        # Botón para descargar el QR
        st.download_button(
            label="Descargar QR",
            data=image_data,
            file_name="qr_generated.png",
            mime="image/png"
        )
    else:
        st.warning("Por favor, introduce una URL.")

    