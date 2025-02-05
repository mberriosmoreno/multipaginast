import streamlit as st

# --- CONFIGURACIÓN DE PÁGINAS ---
def about_me():
    st.title("🏠 Acerca de Mí")
    st.write("""
    Esta es la página "Acerca de Mí". Aquí puedes incluir información sobre ti,
    tu proyecto o cualquier otro detalle relevante.
    """)

def dashboard():
    st.title("📊 Tablero de Datos")
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
    st.title("🤖 Chat Bot")
    st.write("Esta es la página del Chat Bot.")

    # Ejemplo de un chat interactivo
    user_input = st.text_input("Escribe algo:")
    if user_input:
        st.write(f"El bot responde: ¡Hola! Has escrito '{user_input}'.")

# --- MENÚ FIJO CON ICONOS EN LA BARRA LATERAL ---
st.sidebar.markdown("### 🌟 Menú Principal")

# Botones para navegar entre páginas
if st.sidebar.button("🏠 Acerca de Mí"):
    st.session_state.page = "about_me"

if st.sidebar.button("📊 Tablero de Datos"):
    st.session_state.page = "dashboard"

if st.sidebar.button("🤖 Chat Bot"):
    st.session_state.page = "chatbot"

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
try:
    st.image("assets/logo.png", width=300)  # Logo compartido
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo 'logo.png' esté en la carpeta 'assets/'.")

st.sidebar.markdown("Hecho con ❤️ por [Tu Nombre](https://tupagina.com)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if "page" not in st.session_state:
    st.session_state.page = "about_me"  # Página predeterminada

if st.session_state.page == "about_me":
    about_me()
elif st.session_state.page == "dashboard":
    dashboard()
elif st.session_state.page == "chatbot":
    chatbot()
