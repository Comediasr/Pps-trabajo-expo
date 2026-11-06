import streamlit as st

st.title("Pensemos lo visto")
st.subheader("Ahora que investigamos el conjunto de datos y vimos la información que contiene, respondé estas tres preguntas de opción múltiple teniendo en cuenta lo aprendido anteriormente.")

# ============================================================
# Definimos las preguntas
# ============================================================
preguntas = [
    {
        "pregunta": "Cuantos valores unicos tiene la columna type",
        "opciones": ["6", "4", "7"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuales son las 3 provincias con mas aeropuertos",
        "opciones": ["Jujuy, Buenos Aires y Santa fe", "Mendoza, BUenos Aires y Cordoba", "Buenos Aires, Santa Fe y Entre Rios"],
        "correcta": 3
    },
    {
        "pregunta": "¿Que provincia tiene la mayor cantidad de aeropuertos cerrados",
        "opciones": ["Buenos Aires", "Santa Fe", "Santiago del Estero"],
        "correcta": 1
    },
]

# ============================================================
# Una pregunta por bloque, con su propio botón de verificar
# ============================================================
for i, p in enumerate(preguntas):
    st.subheader(f"Pregunta {i + 1}")
    st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("✅ ¡Correcto!")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Incorrecto. La respuesta correcta era: **{correcta}**")

    st.divider()