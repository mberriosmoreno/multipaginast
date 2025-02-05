import streamlit as st

# --- CONFIGURACIÓN DE PÁGINAS ---
about_page = st.Page(
    "views/about_me.py",
    title="Acerca de Mí",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Tablero de Ventas",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# --- CONFIGURACIÓN DE NAVEGACIÓN [CON SECCIONES] ---
pg = st.navigation(
    {
        "Información": [about_page],
        "Proyectos": [project_1_page, project_2_page],
    }
)

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
st.logo("assets/logo.png")
st.sidebar.markdown("Hecho con ❤️ por [Michael Berríos](https://youtube.com/@codingisfun)")

# --- EJECUTAR NAVEGACIÓN ---
pg.run()
