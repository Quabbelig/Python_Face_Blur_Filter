Eine Rastergrafik (auch Bitmap genannt) besteht aus einer Vielzahl einzelner Bildpunkte, sogenannten Pixeln, die in einem rechteckigen Raster angeordnet sind. Jedes Pixel enthält Informationen über die Farbe an einer bestimmten Position im Bild. In den meisten Programmiersprachen wird eine Rastergrafik als mehrdimensionale Datenstruktur, typischerweise als zweidimensionales Array (Matrix) oder als Array von Arrays dargestellt. Dabei entspricht jede Zeile im Array einer horizontalen Pixelreihe im Bild, und jede Spalte einem einzelnen Pixel innerhalb dieser Zeile.

Wenn eine Grafik beispielsweise 800 Pixel breit und 600 Pixel hoch ist, könnte sie in einer Programmiersprache wie Python als bild[600][800] gespeichert werden. Jeder Eintrag in dieser Struktur repräsentiert ein einzelnes Pixel und enthält entweder:
	- einen Grauwert (bei Schwarzweißbildern), meist als Ganzzahl von 0 bis 255,
	- oder ein RGB-Tripel (Rot, Grün, Blau), typischerweise als drei Werte zwischen 0 und 255,
	- optional mit einem vierten Wert für die Transparenz (RGBA).

Beispiel in Python:
```Python
bild = [
    [ [255, 0, 0], [0, 255, 0], [0, 0, 255] ],  # Zeile 1 mit drei RGB-Pixeln
    [ [0, 0, 0], [255, 255, 255], [128, 128, 128] ]  # Zeile 2
]
```
Hier ist bild[0][2] = [0, 0, 255] das dritte Pixel in der ersten Zeile, also ein blaues Pixel.

Diese mehrdimensionale Darstellung ermöglicht es, gezielt auf einzelne Pixel zuzugreifen und diese zu verändern, was für Bildverarbeitung und Computergrafik essenziell ist.
