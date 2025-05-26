import streamlit as st
from PIL import Image #paket für Bilder

import read_data

data = read_data.load_person_data()
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'
    print(st.session_state.current_user)

# Dieses Mal speichern wir die Auswahl als Session State
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = read_data.create_name_list(), key="sbVersuchsperson")


#person_data = read_data.load_person_data()
#data_of_person = read_data.get_person_data_ba_name(person_data, st.session_state.current_user)

person_names = read_data.create_name_list()
try:
    st.session_state.picture_path = read_data.get_person_data_ba_name(data, st.session_state.current_user)["picture_path"]
    if st.session_state.current_user in person_names:
        st.session_state.picture_path = read_data.get_person_data_ba_name(data, st.session_state.current_user)["picture_path"]
except:
    st.session_state.picture_path = "data/pictures/none.jpg"


# Öffne das Bild und Zeige es an
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)

st.write("Der Name ist: ", st.session_state.current_user) 

col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")