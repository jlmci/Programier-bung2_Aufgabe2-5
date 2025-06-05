import json
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'  # Setzt den Standard-Renderer auf den Browser

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])


    def plot_time_series(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        #return self.fig 

    @staticmethod
    def load_by_id(id):
        with open("data/person_db.json") as file:
            person_data = json.load(file)
        ekg_test = None

        for person in person_data:
            for ekg_test_it in person.get("ekg_tests", []):
                #print("Ekg Test:", ekg_test)
                if ekg_test_it["id"] == id:
                    ekg_test = ekg_test_it
                    break
        return ekg_test
   

    def find_peaks(self,  respacing_factor=5):
        """
        A function to find the peaks in a series
        Args:
            - series (pd.Series): The series to find the peaks in
            - threshold (float): The threshold for the peaks
            - respacing_factor (int): The factor to respace the series
        Returns:
            - peaks (list): A list of the indices of the peaks
        """
        # Respace the series
        series = self.df["Messwerte in mV"]
        series = series.iloc[::respacing_factor]

        threshold = series.mean() + 2 * series.std()  # Set threshold as mean + 2*std
        
        # Filter the series
        series = series[series>threshold]


        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in series.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        return peaks
        
    def estimate_heart_rate(self):
        # Wir nehmen die Peaks und berechnen die Herzfrequenz
        peaks = self.find_peaks()
        sample_rate = 500  # 500 Hz
        peak_intervals = np.diff(peaks)  # Abstand in Samples
        rr_intervals_sec = peak_intervals / sample_rate  # Abstand in Sekunden
        bpm_values = 60 / rr_intervals_sec  # Herzfrequenz in BPM

        average_bpm = np.mean(bpm_values)
        return average_bpm
        
    def plot_time_series(self):
        """
        Plot the time series of the EKG data with peak overlay.
        """
        # Zeit relativ zum Start in Sekunden berechnen
        t0 = self.df["Zeit in ms"].iloc[0]
        self.df["Zeit in s"] = (self.df["Zeit in ms"] - t0) / 1000

        # Basis-Linienplot
        self.fig = px.line(
            self.df,
            x="Zeit in s",
            y="Messwerte in mV",
            title=f"EKG Data for ID {self.id}"
        )

        # Initialer Zoombereich: 0–10 Sekunden
        self.fig.update_xaxes(range=[0, 10], title="Zeit (s)")
        self.fig.update_yaxes(title="Messwerte (mV)")

        # ➕ Peaks berechnen
        peaks = self.find_peaks(respacing_factor=5)

        # Zeit- & Messwertwerte der Peaks extrahieren
        peak_times = self.df.loc[peaks, "Zeit in s"]
        peak_values = self.df.loc[peaks, "Messwerte in mV"]

        # ➕ Scatter-Plot für Peaks hinzufügen
        self.fig.add_scatter(
            x=peak_times,
            y=peak_values,
            mode="markers",
            marker=dict(color="red", size=8, symbol="circle"),
            name="Peaks"
        )

        return self.fig




if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    ekg_3_dict = EKGdata.load_by_id(4)
    ekg_3 = EKGdata(ekg_3_dict)
    peaks_in3 = ekg_3.find_peaks()
    #print("Peaks in EKG 3:", peaks_in3)
    ekg_hr = ekg_3.estimate_heart_rate()
    print("Estimated Heart Rate for EKG 3:", ekg_hr)
    fig= ekg_3.plot_time_series()
    fig.show()

    

    #file = open("data/person_db.json")
    #person_data = json.load(file)
    #ekg_dict = person_data[0]["ekg_tests"][0]
    #print(ekg_dict)
    #ekg = EKGdata(ekg_dict)
    #print(ekg.df.head())