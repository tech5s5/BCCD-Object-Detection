# BCCD Object Detection

This project is a web application for detecting RBC (Red Blood Cells), WBC (White Blood Cells), and Platelets in medical images using a fine-tuned YOLOv8 model. The app is built using Gradio and deployed on Hugging Face Spaces.

---

## 🚀 Demo

You can try the live demo here: [Hugging Face Spaces URL](#)

---

## 📂 Project Structure

```
BCCD-object/
│
├── app/
│   ├── app.py                # Gradio app code
│   ├── requirements.txt       # List of dependencies
│
├── model/
│   └── bccd_yolov8.pt         # Trained YOLOv8 model
│
└── dataset.yaml               # YOLOv8 training configuration
```

---

## 🔍 Features

- Upload an image to detect:
  - RBC (Red Blood Cells)
  - WBC (White Blood Cells)
  - Platelets
- Display bounding boxes, labels, and confidence scores.
- User-friendly interface using Gradio.

---

## 📌 Requirements

Add these packages to your `requirements.txt` file:

```
ultralytics
gradio
torch
Pillow
```

---

## 📖 Usage

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BCCD-Object-Detection.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
python app/app.py
```

---

## 📤 Deployment on Hugging Face Spaces

1. Upload the following files to your Hugging Face Space:
   - `app/app.py`
   - `app/requirements.txt`
   - `model/bccd_yolov8.pt`
2. Click **Commit changes** and wait for the app to build.

---

## 📌 Submission Requirements

- GitHub Repository: Provide a link to this repository.
- Hugging Face Spaces URL: Provide the URL of your deployed app.

---

## 📧 Contact

For any queries, reach out at: tech2345s55\@gmail.com

