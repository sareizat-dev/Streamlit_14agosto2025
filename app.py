import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Configuración de la página
st.set_page_config(page_title="Agente con Llama3-8B", page_icon="🤖", layout="centered")

st.title("🤖 Agente LangChain + Groq (Llama3-8B-8192)")

# Entrada de API Key
groq_api_key = st.text_input(
    "Introduce tu GROQ API Key:",
    type="password",
    help="Puedes obtener tu API Key en https://console.groq.com/"
)

# Inicializar LLM solo si hay API Key
if groq_api_key:
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model="llama3-8b-8192",
        temperature=0.7,
        max_tokens=512
    )

    # Plantilla de prompt
    prompt_template = ChatPromptTemplate.from_template(
        "Eres un asistente experto en análisis de datos y salud en Colombia. "
        "Responde de forma clara y detallada la siguiente consulta:\n\n{pregunta}"
    )

    # Crear el Chain
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Interfaz de usuario
    st.subheader("Haz una pregunta")
    pregunta_usuario = st.text_area("Escribe aquí tu consulta:", height=120)

    if st.button("Enviar", type="primary"):
        if pregunta_usuario.strip():
            with st.spinner("Pensando... 💭"):
                respuesta = chain.run(pregunta=pregunta_usuario)
            st.markdown("### Respuesta:")
            st.write(respuesta)
        else:
            st.warning("Por favor ingresa una pregunta antes de enviar.")
else:
    st.info("🔑 Por favor, introduce tu GROQ API Key para comenzar.")

st.caption("Powered by LangChain + Groq + Llama3-8B-8192")


