import streamlit as st
from PIL import Image #paket für Bilder

import read_data
import read_pandas # Importiere die Funktionen aus read_data.py
# Importiere die Funktionen aus read_data.py
# Lade die Personendaten und die Namensliste
data = read_data.load_person_data()
person_names = read_data.create_name_list()

# App Titel
st.write("# EKG APP")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'


#Oberste Zeile des programms
ueberschrift, person_auswahl = st.columns([1,2], gap="small")
with ueberschrift:
    st.markdown("<div style='padding-top: 23px; font-size: 32px;'>Dashboard von</div>", unsafe_allow_html=True)
with person_auswahl:
    st.session_state.current_user = st.selectbox('', options = read_data.create_name_list())

#st.markdown("<br>", unsafe_allow_html=True)  # Leerer Platzhalter, um den Abstand zu vergrößern


try:
    st.session_state.picture_path = read_data.get_person_data_ba_name(data, st.session_state.current_user)["picture_path"]
    if st.session_state.current_user in person_names:
        st.session_state.picture_path = read_data.get_person_data_ba_name(data, st.session_state.current_user)["picture_path"]
except:
    st.session_state.picture_path = "data/pictures/none.jpg"
image = Image.open(st.session_state.picture_path)



id_value = read_data.get_person_data_ba_name(data, st.session_state.current_user)["id"]
birthdate_value = read_data.get_person_data_ba_name(data, st.session_state.current_user)["date_of_birth"]
# Bild und Personendaten nebeneinander anzeigen
bild, personendaten = st.columns([1,2], gap="small")
with bild:
    st.markdown("<div style='padding-top: 23px; font-size: 32px;'>Personendaten</div>", unsafe_allow_html=True)
    st.image(image)
with personendaten:
    st.markdown("<br><br>", unsafe_allow_html=True) # Leerer Platzhalter, um den Abstand zu vergrößern
    st.write("Vorname: ", read_data.get_person_data_ba_name(data, st.session_state.current_user)["firstname"])
    st.write("Nachname: ", read_data.get_person_data_ba_name(data, st.session_state.current_user)["lastname"])
    st.markdown(f"<span style='color:white; font-size:16px;'>id: {id_value}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:white; font-size:16px;'>id: {birthdate_value}</span>", unsafe_allow_html=True)
    st.write("Geschlecht: ", read_data.get_person_data_ba_name(data, st.session_state.current_user)["gender"])


st.write("## EKG-Daten")
data_plot = read_pandas.read_my_csv()   #lese die EKG-Daten ein
fig = read_pandas.make_plot(data_plot)
#st.write(fig)  # Erstelle den Plot
st.plotly_chart(fig)  # Zeige den Plot in der Streamlit-App an



Leistung_mean, leer = st.columns([1,1], gap="small")
with Leistung_mean:
    st.markdown("<div style='padding-top: 23px; font-size: 32px;'>Leistung</div>", unsafe_allow_html=True)
    st.write("Mittelwert: ", read_pandas.mittelwerte(data_plot)[0])
    st.write("Maximalwert: ", read_pandas.mittelwerte(data_plot)[1])

    
# Hier können Sie die EKG-Daten anzeigen, die zu der ausgewählten Person gehören

