
# Face Detection and Recognition System

This project is a **real-time face detection and recognition system** built using Python, OpenCV, and the `face_recognition` library. 
It detects human faces from live camera feeds, encodes them into unique numerical vectors, and matches them against a pre-existing database of known faces.

## 🚀 Features
- Real-time face detection using OpenCV
- Face recognition using deep learning embeddings (`face_recognition` library)
- Dynamic database update with new faces
- Displays bounding boxes and labels for recognized faces
- Cost-effective and scalable (runs on consumer-grade hardware)
- Applications in **surveillance, attendance tracking, and access control**

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: OpenCV, face_recognition, NumPy
- **Hardware**: Standard laptop/desktop with webcam

## 📂 Project Structure
```
├── main.py               # Runs the face recognition system with live video feed
├── simple_facerec.py     # Helper class for encoding and detecting faces
├── images/               # Folder containing known face images (database)
└── README.md             # Project documentation
```

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-recognition-system.git
   cd face-recognition-system
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add known faces to the `images/` folder. Each image should be named as the person's name (e.g., `John.jpg`).

5. Run the program:
   ```bash
   python main.py
   ```

## 📊 Workflow
1. Data Collection (images or live camera feed)
2. Image Preprocessing (resizing, grayscale conversion)
3. Face Detection (locating faces using OpenCV/Deep Learning)
4. Face Encoding (CNN-based feature extraction)
5. Face Matching & Recognition (comparing embeddings)
6. Real-Time Display with bounding boxes & labels
7. Database Updates for new faces

## 📸 Sample Output
- Detects faces in real-time from webcam
- Labels recognized faces with names
- Unknown faces are marked as **Unknown**

## 🔮 Future Enhancements
- Improve recognition accuracy under masks/occlusions
- Integration with cloud-based face databases
- Mobile and IoT deployment
- Add GUI for user-friendly interaction

## 📖 References
- [OpenCV Documentation](https://docs.opencv.org/)
- [Face Recognition Library](https://github.com/ageitgey/face_recognition)
- *Pattern Recognition and Machine Learning* - C. M. Bishop
- *Deep Learning* - Ian Goodfellow, Yoshua Bengio, Aaron Courville

---
👨‍💻 Developed by [Your Name]
