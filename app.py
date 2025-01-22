import streamlit as st
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

st.title("🧠 Ferramenta de Pergunta e Resposta")

col1, col2 = st.columns([3, 1])

with col1:
    context = st.text_area("📄 Digite o texto para a pergunta:", height=200)
    question = st.text_input("❓ Digite a pergunta:")

with col2:
    st.markdown("### Resposta:")
    answer_box = st.empty() 

if st.button("🔍 Responder"):
    if context and question:
        answer = answer_question(context, question)
        answer_box.markdown(f"**Resposta:** {answer}")
    else:
        st.error("Por favor, forneça tanto o texto quanto a pergunta.")

st.markdown("---")
