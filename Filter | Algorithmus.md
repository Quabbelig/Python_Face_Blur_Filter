In der dargestellten Anwendung wird ein Weichzeichnungsfilter (Blur-Filter) verwendet, um Gesichter in Bildern oder einem Live-Webcam-Stream unkenntlich zu machen. Konkret wird dabei der Box-Blur bzw. Gleichgewichtige Mittelwertfilter aus OpenCV mit der Funktion cv2.blur() eingesetzt.

# Funktionsweise:

Der Blur-Filter arbeitet folgendermaßen:

- Für jeden Pixel innerhalb des Zielbereichs (z. B. Gesicht) wird ein sogenannter Kernel (eine quadratische Matrix mit ungeraden Seitenlängen, z. B. 35x35 Pixel) über das Bild geschoben.
- Innerhalb dieses Bereichs wird der Durchschnitt aller Pixelwerte berechnet.
- Der zentrale Pixel des Bereichs erhält anschließend diesen Durchschnittswert.
- Dieser Vorgang wiederholt sich für jeden Pixel im markierten Bereich, wodurch ein glattes, verschwommenes Aussehen entsteht.

Durch diesen Vorgang werden Details im Gesicht, wie Augen, Mund oder Nase, zunehmend unkenntlich, je größer der Kernel ist.

## Anwendung im Programm:

  **1.	Gesichtserkennung:**
 - Die Anwendung nutzt das cvzone.FaceDetectionModule, welches intern auf MediaPipe basiert, um Gesichter im Bild oder Videoframe zu erkennen.
 - Die Funktion fd.findFaces() liefert für jedes erkannte Gesicht eine bbox (Bounding Box) mit den Koordinaten und Abmessungen des Gesichts.
	**2.	Unschärfe anwenden:**
 - Um die erkannten Gesichter wird ein erweiterter Bereich (abhängig vom einstellbaren margin) ausgeschnitten.
 - Auf diesen Bildausschnitt wird dann der Blur-Filter mit einem anpassbaren Kernel (ksize) angewendet.
 - Das unscharfe Gesicht wird anschließend in das Bild zurückgesetzt, wodurch es effektiv unkenntlich gemacht ist.
	**3.	Dynamische Anpassung:**
 - Die Unschärfe-Intensität lässt sich über einen Schieberegler steuern. Dabei beeinflusst der hidden_level sowohl die Größe des unscharf gemachten Bereichs (margin) als  auch die Stärke der Unschärfe (ksize).
 - Die Kernelgröße (ksize) wird so berechnet, dass sie stets eine ungerade Zahl bleibt, was eine Voraussetzung für viele OpenCV-Filter ist.
