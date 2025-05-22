import streamlit as st
import read_data

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Dieses Mal speichern wir die Auswahl als Session State
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = read_data.create_name_list(), key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user) 
