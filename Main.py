import cv2
from cvzone.FaceDetectionModule import FaceDetector
import tkinter as tk
from tkinter import filedialog, messagebox

class BlurApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Select Blur Mode")
        self.mode = None
        self.hidden_level = 0
        self.margin = 0
        self.ksize = 35
        self.fd = FaceDetector()
        self.show_box = tk.BooleanVar(value=False)
        self.image = None
        self.preview = None
        tk.Label(root, text="Choose blur mode:", font=("Arial", 14)).pack(pady=10)
        tk.Button(root, text="Blur Picture", width=20, command=lambda: self.select_mode("picture")).pack(pady=5)
        tk.Button(root, text="Blur Live (Webcam)", width=20, command=lambda: self.select_mode("live")).pack(pady=5)
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

    def select_mode(self, mode):
        self.mode = mode
        self.status_label.config(text=f"Selected mode: {mode}")
        self.update_blur_params()
        if self.mode == "live":
            self.start_live()
        elif self.mode == "picture":
            self.start_picture()
        else:
            messagebox.showinfo("Info", "Wtf???") #remove later, only for debugging!!!!
            self.root.destroy()

    def show_detection_checkbox(self):
        self.cb = tk.Checkbutton(
            self.root,
            text="Show detection box and confidence",
            variable=self.show_box,
            onvalue=True,
            offvalue=False,
            command=self.on_detection_box_toggle)
        self.cb.pack(pady=2)

    def show_hiddenness_slider(self):
        if hasattr(self, 'slider_frame'):
            self.slider_frame.destroy()
        self.slider_frame = tk.Frame(self.root)
        self.slider_frame.pack(pady=5)
        self.hiddenness_var = tk.StringVar(value=str(self.hidden_level))
        self.hiddenness_entry = tk.Entry(self.slider_frame, width=6, textvariable=self.hiddenness_var, justify='center')
        self.hiddenness_entry.pack(side='left', padx=5)

        def on_entry_change(*args):
            val = self.hiddenness_var.get()
            try:
                fval = float(val)
                if 0 <= fval <= 100:
                    self.hidden_level = fval
                    self.slider.set(fval)
                    self.update_blur_params()
                    if self.mode == "picture":
                        self.show_picture_preview()
                else:
                    pass
            except ValueError:
                pass
        self.hiddenness_var.trace_add('write', on_entry_change)
        self.slider = tk.Scale(self.slider_frame, from_=0, to=100, orient="horizontal", length=300, command=self.on_slider_change)
        self.slider.set(self.hidden_level)
        self.slider.pack(side='left')

    def on_slider_change(self, val):
        try:
            self.hidden_level = float(val)
            if hasattr(self, 'hiddenness_var'):
                current = self.hiddenness_var.get()
                new_val = f"{self.hidden_level:.2f}"
                if current != new_val:
                    self.hiddenness_var.set(new_val)
            self.update_blur_params()
            if self.mode == "picture":
                self.show_picture_preview()
        except ValueError:
            pass

    def update_blur_params(self):
        t = self.hidden_level / 100  # Now allows 0
        self.margin = int(t * 150)
        self.ksize = int(1 + t * (175 - 1))  # from 1 to 175
        if self.ksize % 2 == 0:
            self.ksize += 1

    def start_live(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
        self.show_hiddenness_slider()
        self.show_detection_checkbox()
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam")
            return
        self.running = True
        self.latest_frame = None
        self.root.after(10, self.update_live_frame)  # Start loop

    def update_live_frame(self):
        if not self.running:
            if self.cap.isOpened():
                self.cap.release()
            cv2.destroyAllWindows()
            self.root.destroy()
            return
        ret, frame = self.cap.read()
        if not ret:
            self.running = False
            self.root.after(10, self.update_live_frame)
            return
        img, faces = self.fd.findFaces(frame, draw=False)
        output = frame.copy()
        if not hasattr(self, 'last_bbox'):
            self.last_bbox = None
        if faces:
            self.last_bbox = faces[0]["bbox"]  # Only use the first face for fallback
            for face in faces:
                x, y, w, h = face["bbox"]
                x1 = max(0, x - self.margin)
                y1 = max(0, y - self.margin)
                x2 = min(output.shape[1], x + w + self.margin)
                y2 = min(output.shape[0], y + h + self.margin)
                face_img = output[y1:y2, x1:x2]
                face_img = cv2.blur(face_img, (self.ksize, self.ksize))
                output[y1:y2, x1:x2] = face_img
        elif self.last_bbox:
            x, y, w, h = self.last_bbox
            x1 = max(0, x - self.margin)
            y1 = max(0, y - self.margin)
            x2 = min(output.shape[1], x + w + self.margin)
            y2 = min(output.shape[0], y + h + self.margin)
            face_img = output[y1:y2, x1:x2]
            face_img = cv2.blur(face_img, (self.ksize, self.ksize))
            output[y1:y2, x1:x2] = face_img
        if self.show_box.get() and (faces or self.last_bbox):
            targets = faces if faces else [{"bbox": self.last_bbox, "score": [0]}]
            for face in targets:
                x, y, w, h = face["bbox"]
                conf = int(face["score"][0] * 100) if "score" in face else 0
                cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 255), 2)
                cv2.putText(output, f'{conf}%', (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
        cv2.imshow("Live Blur (Press ESC to exit)", output)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            self.running = False
            self.cap.release()
            cv2.destroyAllWindows()
            self.root.destroy()
            return
        self.root.after(10, self.update_live_frame)

    def on_detection_box_toggle(self):
        if self.mode == "picture":
            self.show_picture_preview()

    def live_blur_loop(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                self.running = False
                break
            img, faces = self.fd.findFaces(frame, draw=False)
            self.latest_frame = frame.copy()
            if faces:
                for face in faces:
                    x, y, w, h = face["bbox"]
                    x1 = max(0, x - self.margin)
                    y1 = max(0, y - self.margin)
                    x2 = min(frame.shape[1], x + w + self.margin)
                    y2 = min(frame.shape[0], y + h + self.margin)
                    face_img = self.latest_frame[y1:y2, x1:x2]
                    face_img = cv2.blur(face_img, (self.ksize, self.ksize))
                    self.latest_frame[y1:y2, x1:x2] = face_img
            if self.show_box.get() and faces:
                for face in faces:
                    x, y, w, h = face["bbox"]
                    conf = int(face["score"][0] * 100)
                    cv2.rectangle(self.latest_frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
                    cv2.putText(self.latest_frame, f'{conf}%', (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
            cv2.imshow("Live Blur (Press ESC to exit)", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC pressed
                self.running = False
                self.cap.release()
                cv2.destroyAllWindows()
                self.slider.destroy()
                self.root.destroy()
                return
            self.root.after(10, self.live_blur_loop)

    def start_picture(self):
        path = filedialog.askopenfilename(title="Select an image",
                                          filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if not path:
            self.root.destroy()
            return
        for widget in self.root.pack_slaves():
            widget.destroy()
        self.show_hiddenness_slider()
        self.show_detection_checkbox()
        self.image = cv2.imread(path)
        self.show_picture_preview()
        self.build_picture_controls()

    def check_picture_window(self):
        if cv2.getWindowProperty("Picture Preview", cv2.WND_PROP_VISIBLE) < 1:
            cv2.imshow("Picture Preview", self.preview)
        self.root.after(100, self.check_picture_window)

    def show_picture_preview(self):
        img = self.image.copy()
        img = self.apply_blur_to_all_faces(img)
        self.preview = img
        cv2.imshow("Picture Preview", img)
        self.check_picture_window()

    def apply_blur_to_all_faces(self, img):
        img, faces = self.fd.findFaces(img, draw=False)
        if faces:
            for f in faces:
                x, y, w, h = f["bbox"]
                x1, y1 = max(x - self.margin, 0), max(y - self.margin, 0)
                x2, y2 = min(x + w + self.margin, img.shape[1]), min(y + h + self.margin, img.shape[0])
                roi = img[y1:y2, x1:x2]
                img[y1:y2, x1:x2] = cv2.blur(roi, (self.ksize, self.ksize))
        if self.show_box.get():
            for face in faces:
                x, y, w, h = face["bbox"]
                conf = int(face["score"][0] * 100)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                cv2.putText(img, f'{conf}%', (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
        return img

    def build_picture_controls(self):
        tk.Button(self.root, text="Done", command=self.picture_done).pack(pady=5)

    def picture_done(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
        tk.Button(self.root, text="Back", command=self.reset_picture).pack(pady=5)
        tk.Button(self.root, text="Save", command=self.save_picture).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)

    def reset_picture(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
        self.show_hiddenness_slider()
        self.show_detection_checkbox()
        self.build_picture_controls()
        self.show_picture_preview()

    def apply_blur_to_all_faces_no_boxes(self, img):
        img, faces = self.fd.findFaces(img, draw=False)
        if faces:
            for f in faces:
                x, y, w, h = f["bbox"]
                x1, y1 = max(x - self.margin, 0), max(y - self.margin, 0)
                x2, y2 = min(x + w + self.margin, img.shape[1]), min(y + h + self.margin, img.shape[0])
                roi = img[y1:y2, x1:x2]
                img[y1:y2, x1:x2] = cv2.blur(roi, (self.ksize, self.ksize))
        return img

    def save_picture(self):
        if self.image is None:
            return
        clean_img = self.image.copy()
        clean_img = self.apply_blur_to_all_faces_no_boxes(clean_img)

        path = filedialog.asksaveasfilename(title="Save image", defaultextension=".png",
                                            filetypes=[("PNG", "*.png"), ("JPG", "*.jpg")])
        if path:
            cv2.imwrite(path, clean_img)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BlurApp(root)
    root.mainloop()