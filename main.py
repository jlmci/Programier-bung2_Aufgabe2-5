import streamlit as st
from PIL import Image #paket für Bilder

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


#person_data = read_data.load_person_data()
#data_of_person = read_data.get_person_data_ba_name(person_data, st.session_state.current_user)

person_names = read_data.create_name_list
if st.session_state.current_user in person_names:
    st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]

# ...

# Öffne das Bild und Zeige es an
image = Image.open("../" + st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)

st.write("Der Name ist: ", st.session_state.current_user) 

#image = Image.open(data_of_person["picture_path"])
#st.image(image, caption=st.session_state.current_user)