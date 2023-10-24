import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Music Mixer", page_icon="🎵")

# Título de la página
st.title("Bienvenido a Music Mixer")

# Sección de la página principal
if st.button("Ir a la aplicación"):
    st.write("¡Vamos a mezclar música!")
    st.write("Selecciona las canciones que deseas mezclar y crea tu propia playlist.")

# Sección de la aplicación
if st.button("Usar la aplicación"):
    st.header("Aplicación Music Mixer")
    st.write("Esta aplicación te permite mezclar tus canciones y crear playlists personalizadas.")
    # Aquí agregarías la funcionalidad de la aplicación para mezclar canciones.

# Sección del creador
if st.button("Acerca del creador"):
    st.header("Acerca del creador")
    st.write("Esta aplicación fue creada por David Olguín.")
    st.write("Si tienes alguna pregunta o comentario, puedes contactarme en david@example.com")

# Nota explicativa
st.write("Nota: Esta es una versión de demostración. La funcionalidad real de mezcla de música no está implementada en este ejemplo.")

