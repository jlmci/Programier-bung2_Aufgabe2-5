# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np


# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/activities/activity.csv", sep=",", usecols=["HeartRate","PowerOriginal"], header = 0)

    df["Zeit"] = np.arange(0, len(df))  # Erstelle eine Zeitspalte in Millisekunden

    #print(df.head())
    
    # Gibt den geladen Dataframe zurück
    return df


# %%

def make_plot(df):


    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df, x= "Zeit", y="HeartRate", title="Herzfrequenz über Zeit")
    
    return fig

#%% Test
if __name__ == "__main__":
    # Teste die Funktionen
    df = read_my_csv()
    fig = make_plot(df)
    
    # Zeige den Plot an
    fig.show()


# %%
