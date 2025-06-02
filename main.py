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




st.write("## Leistungstest")

if "max_hr_input_user" not in st.session_state:
    st.session_state.max_hr_input_user = 180  # Standardwert für die maximale Herzfrequenz


max_hf, max_hf_einstellen = st.columns([18,3], gap="small")
with max_hf:
    st.markdown("<div style='padding-top: 27px; font-size: 21px;'>Maximale Herzfrequenz (nur Wert zwischen 160 und 210 eingeben)</div>", unsafe_allow_html=True)
with max_hf_einstellen:
    user_input_str = st.text_input(
    label="",
    value=str(st.session_state.max_hr_input_user),
    key="max_hr_input_widget")

try:
    user_input_value = int(user_input_str)
    if user_input_value < 160 or user_input_value > 210:
        st.error("Bitte gib eine Zahl zwischen 160 und 210 ein.")
except:
    pass


try:
    new_hr_value = int(user_input_str)
    if new_hr_value != st.session_state.max_hr_input_user:
        st.session_state.max_hr_input_user = new_hr_value
except ValueError:
    st.error("Bitte gib eine gültige Zahl für die Herzfrequenz ein.")





data_plot = read_pandas.read_my_csv()   #lese die EKG-Daten ein
zone1, zone2, zone3, zone4, zone5, df, zone_boundries = read_pandas.calculate_HR_zone(data_plot, int(st.session_state.max_hr_input_user))
fig = read_pandas.make_plot(df)  # Erstelle den Plot

#st.write(fig)  # Erstelle den Plot
st.plotly_chart(fig)  # Zeige den Plot in der Streamlit-App an





Leistung_mean, hr_zones, time_in_hr_zones = st.columns([1,1,1], gap="small")
with Leistung_mean:
    st.markdown("<div style='padding-top: 0px; font-size: 21px;'>Leistungsdaten (Watt)</div>", unsafe_allow_html=True)
    st.write("Mittelwert: ", read_pandas.mittelwerte(data_plot)[0].round(2))
    st.write("Maximalwert: ", read_pandas.mittelwerte(data_plot)[1].round(2))
    st.write("Mittelwert in Zone 1: ", round(zone1["PowerOriginal"].mean(),2))
    st.write("Mittelwert in Zone 2: ", round(zone2["PowerOriginal"].mean(),2))
    st.write("Mittelwert in Zone 3: ", round(zone3["PowerOriginal"].mean(),2))
    st.write("Mittelwert in Zone 4: ", round(zone4["PowerOriginal"].mean(),2))
    st.write("Mittelwert in Zone 5: ", round(zone5["PowerOriginal"].mean(),2))

with hr_zones:
    st.markdown("<div style='padding-top: 0px; font-size: 21px;'>Herzfrequenz (bpm)</div>", unsafe_allow_html=True)
    st.write("Mittelewert", df["HeartRate"].mean().round(2))
    st.write("Maximal: ", df["HeartRate"].max().round(2))
    st.write("Mittelwert von Zone 1: ", round(zone1["HeartRate"].mean(),2))
    st.write("Mittelwert von Zone 2: ", round(zone2["HeartRate"].mean(),2))
    st.write("Mittelwert von Zone 3: ", round(zone3["HeartRate"].mean(),2))
    st.write("Mittelwert von Zone 4: ", round(zone4["HeartRate"].mean(),2))
    st.write("Mittelwert von Zone 5: ", round(zone5["HeartRate"].mean(),2))    

with time_in_hr_zones:
    st.markdown("<div style='padding-top: 0px; font-size: 21px;'>Zeit (s)</div>", unsafe_allow_html=True)
    st.write("gesamte Zeit: ", len(df))
    st.markdown("<div style='padding-top: 40px; font-size: 21px;'></div>", unsafe_allow_html=True)
    st.write("Zeit in Zone 1: ", len(zone1))
    st.write("Zeit in Zone 2: ", len(zone2))
    st.write("Zeit in Zone 3: ", len(zone3))
    st.write("Zeit in Zone 4: ", len(zone4))
    st.write("Zeit in Zone 5: ", len(zone5))
# Hier können Sie die EKG-Daten anzeigen, die zu der ausgewählten Person gehören

