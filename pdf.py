import streamlit as st
import base64

pdf_files = {}

uploaded_files = st.file_uploader("Envie seus arquivos PDF", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        pdf_data = uploaded_file.read()
        pdf_files[uploaded_file.name] = pdf_data

    filtered_files = [name for name in pdf_files.keys() ]
    selected_file = st.selectbox("Selecione um arquivo PDF para visualizar:", options=filtered_files)

    if selected_file:
        selected_pdf_data = pdf_files[selected_file]

        base64_pdf = base64.b64encode(selected_pdf_data).decode('utf-8')

        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        st.write(f"Você está visualizando: **{selected_file}**")
    else:
        st.write("Nenhum arquivo encontrado com o nome pesquisado.")
