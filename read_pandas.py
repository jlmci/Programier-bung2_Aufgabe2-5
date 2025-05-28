# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np


# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'  # Setzt den Standard-Renderer auf den Browser

def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/activities/activity.csv", sep=",", usecols=["HeartRate","PowerOriginal"], header = 0)

    df["Zeit"] = np.arange(0, len(df))  # Erstelle eine Zeitspalte in Millisekunden
    

    return df

def calculate_HR_zone(df, max_Hr_input):
  df["HeartZone"] = ""

  for index, observation in df.iterrows():
    if observation["HeartRate"] < max_Hr_input * 0.6:
      heartzone = "Zone 1"
    elif observation["HeartRate"] >= max_Hr_input*0.6 and observation["HeartRate"] < max_Hr_input * 0.75:
      heartzone = "Zone 2"
    elif observation["HeartRate"] >= max_Hr_input * 0.75 and observation["HeartRate"] < max_Hr_input * 0.85:
      heartzone = "Zone 3"
    elif observation["HeartRate"] >= max_Hr_input * 0.85 and observation["HeartRate"] < max_Hr_input * 0.95:
      heartzone = "Zone 4"
    else:
      heartzone = "Zone 5"   
    
    df.at[index, 'HeartZone'] = heartzone


  # making boolean series for a team name
  filter_Zone1 = df.where(df["HeartZone"]=="Zone 1")
  filter_Zone1.dropna()
    
  # making boolean series for age
  filter_Zone2 = df.where(df["HeartZone"]=="Zone 2")
  filter_Zone2.dropna()

  filter_Zone3 = df.where(df["HeartZone"]=="Zone 3")
  filter_Zone3.dropna()

  filter_Zone4 = df.where(df["HeartZone"]=="Zone 4")
  filter_Zone4.dropna()

  filter_Zone5 = df.where(df["HeartZone"]=="Zone 5")
  filter_Zone5.dropna()


def make_plot(df):
    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df, x= "Zeit", y=["HeartRate", "PowerOriginal"])
    
    return fig

def mittelwerte(df):
    # Berechnet den Mittelwert der Spalten "HeartRate" und "PowerOriginal"
    power_original_mean = df["PowerOriginal"].mean()
    power_original_max = df["PowerOriginal"].max()
    
    return power_original_mean , power_original_max


    
if __name__ == "__main__":
    df = read_my_csv()
    fig = make_plot(df)
    fig.show()

# %%
