import streamlit as st

# --- CONFIGURACIÓN DE PÁGINAS ---
about_page = st.Page(
    "Pages/about_me.py",
    title="Acerca de Mí",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "Pages/sales_dashboard.py",
    title="Tablero de Ventas",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "Pages/chatbot.py",
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
st.logo("assets/codingisfun_logo.png")
st.sidebar.markdown("Hecho con ❤️ por [Sven](https://youtube.com/@codingisfun)")

# --- EJECUTAR NAVEGACIÓN ---
pg.run()
