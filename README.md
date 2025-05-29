# Programier-bung2_Aufgabe2-5
## Aufgabe 2
### Vorarbeit
Zu Beginn sollte ein Use-Case-Diagramm, ein Activity Diagramm, sowie ein Mock up vom Dashboard erstellt werden.
Hier grob als Handskizzen:
- Use Case Diagramm:
![Diagramm](pictures_readme/Use_case.png)
- Activity Diagramm:
![Diagramm](pictures_readme/Activity.png)
- Mock Up:
![Diagramm](pictures_readme/mockup.png)

### Umsetzung
Nach erstellen einer read_data.py, in der die Daten geladen werden und es auch eine Funktion erstellt wurde, die ein Suchen der Daten einer Person ermöglicht, ging es daran das Mockup nachzubauen.

Schwierig war es dabei vor allem es so einzurichten, dass der Name der Person, dessen Dashboard angezeigt wird auch gleichzeitig das Auswahlfenster der Personen ist (wie es das Mockup vorgab)

### Ergebnis
Nach Aufgabe 2 hat das Programm folgendes aussehen:
![Diagramm](pictures_readme/nach_Aufgabe_2.png)


## Aufgabe 3
### Beschreibung
Die App kann interaktiv nach Namensauswahl Personendaten und Bild einer im Datensatz gespeicherten Person ausgeben und präsentieren (Aufgabe 2).

Weiter wird unten ein Plot eines Leistungstests mit Herzfrequenz, welche nach Belastungsstufe, welche davor eingegeben werden kann, eingefärbt ist. Außerdem gibt es dort überlagernd einen Plot, welcher der die erbrachte Leistung anzeigt.

Unter dem Plot finden sich noch weitere Werte, wie Durchschnittsleistung und Zeit verbracht pro Herzfrequenzzone.

### Benutzung
Die App wird gestartet, indem man im Terminal "streamlit run main.py" eingibt. Dann kann man bei "Dashboard von" die zu betrachtende Person aus einem dropdown Menü auswählen. Über den Daten des Leistungstests kann man die maximale Herzfrequenz eingeben - der Wert ist zuerst standardmäßig auf 180bpm gesetzt.

In dem Plot kann man belibig über die Datenpunkte hovern um genaue Werte zu erhalten, oben rechts vom Plot gibt es noch weitere Funktionen, wie speichern als png und Zoomen.

### Ergebnis
Nach Aufgabe 3 schaut das Programm wiefolgt aus:
![Diagramm](pictures_readme/nach_Aufgabe_3.png)
