README.md

# Hand-Drawn Image Recognition using CNN and Flask

## 🧠 Project Overview
This project is a deep learning-based web application that recognizes hand-drawn digits and sketches. It uses a Convolutional Neural Network (CNN) built with TensorFlow and Keras to classify images drawn by the user or uploaded as files. OpenCV is used for image preprocessing such as grayscale conversion, resizing, and noise removal. The model is integrated into a Flask web app for real-time prediction through an interactive web interface.

---

## ⚙️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Canvas for drawing)
- **Backend:** Flask (Python)
- **Machine Learning:** TensorFlow, Keras, OpenCV, NumPy
- **Dataset:** MNIST and Google QuickDraw

---

## 🚀 Features
- Draw digits or sketches on a web canvas for prediction  
- Upload an image for recognition  
- Real-time prediction using CNN model  
- Preprocessing pipeline with OpenCV  
- Simple and clean web interface  

---

## 🧩 Project Structure

hand-drawn-image-recognition/ │ ├── app.py                # Flask main file ├── model.h5              # Trained CNN model ├── preprocess.py         # Image preprocessing script ├── requirements.txt      # Python dependencies │ ├── static/               # CSS, JS, demo images │   └── style.css │ ├── templates/            # HTML templates │   ├── index.html │   └── result.html │ └── uploads/              # Uploaded images folder

---

## 🛠️ Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hand-drawn-image-recognition.git
   cd hand-drawn-image-recognition

2. Install dependencies:

pip install -r requirements.txt


3. Run the Flask app:

python app.py


4. Open your browser and go to:

http://127.0.0.1:5000/




---

📦 Dependencies

List of main libraries used:

Flask
TensorFlow
Keras
OpenCV-Python
NumPy
Pillow


---

🎯 Future Enhancements

Support for multiple drawing categories

Model optimization for faster predictions

Integration with cloud deployment



---

📸 Demo
![alt text](<Screenshot (1).png>) ![alt text](<Screenshot (2).png>) ![alt text](<Screenshot 2025-11-01 114759.png>) ![alt text](<Screenshot 2025-11-01 114829.png>) ![alt text](<Screenshot 2025-11-01 114952.png>) ![alt text](<Screenshot 2025-11-01 115040.png>)




---

📎 Model File

If your model file is too large for GitHub, you can upload it to Google Drive and share the link here:
👉 Download Trained Model


---

👩‍💻 Author

Abhilash V Dhavale
Email: abhilashdhavale52@gmail.com
GitHub: https://github.com/AbhilashDhavale