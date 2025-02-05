import streamlit as st

# --- CONFIGURACIÓN DE PÁGINAS ---
# Definir las páginas de la aplicación como funciones
def about_me():
    st.title("Acerca de Mí")
    st.write("""
    Esta es la página "Acerca de Mí". Aquí puedes incluir información sobre ti,
    tu proyecto o cualquier otro detalle relevante.
    """)

def dashboard():
    st.title("Tablero de Datos")
    st.write("Esta es la página del tablero de datos.")

    # Ejemplo de un DataFrame
    import pandas as pd
    data = {
        "Nombre": ["Juan", "María", "Pedro"],
        "Edad": [25, 30, 35],
        "Ciudad": ["Madrid", "Barcelona", "Valencia"],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

def chatbot():
    st.title("Chat Bot")
    st.write("Esta es la página del Chat Bot.")

    # Ejemplo de un chat interactivo
    user_input = st.text_input("Escribe algo:")
    if user_input:
        st.write(f"El bot responde: ¡Hola! Has escrito '{user_input}'.")

# --- MENÚ DE NAVEGACIÓN ---
# Crear un menú desplegable en la barra lateral para seleccionar la página
page = st.sidebar.selectbox(
    "Selecciona una página",
    ["Acerca de Mí", "Tablero de Datos", "Chat Bot"]
)

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
# Agregar un logo en la parte superior (asegúrate de que esta imagen exista en la carpeta "assets/")
try:
    st.image("assets/logo.png", use_column_width=True)  # Logo compartido
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo 'logo.png' esté en la carpeta 'assets/'.")

# Mensaje en la barra lateral
st.sidebar.markdown("Hecho con ❤️ por [Tu Nombre](https://tupagina.com)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if page == "Acerca de Mí":
    about_me()
elif page == "Tablero de Datos":
    dashboard()
elif page == "Chat Bot":
    chatbot()
