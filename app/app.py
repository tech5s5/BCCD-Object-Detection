import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load the trained model
model = YOLO('bccd_yolov8.pt')  # Make sure the model file is in the same folder as app.py

# Prediction function
def predict(image):
    results = model(image)
    annotated_image = results[0].plot()  # Draw bounding boxes
    return Image.fromarray(annotated_image)

# Gradio Interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="BCCD Object Detection",
    description="Upload an image to detect RBC, WBC, and Platelets.",
)

iface.launch()
