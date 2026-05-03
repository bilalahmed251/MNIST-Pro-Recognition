import streamlit as st
from streamlit_drawable_canvas import st_canvas
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import numpy as np
from model import get_model
import os

# Page configuration
st.set_page_config(page_title="Handwritten Digit Recognition", layout="centered")

# Custom CSS for premium look
st.markdown("""
    <style>
        .main {
                background-color: #0e1117;
                        color: #ffffff;
                            }
                                .stButton>button {
                                        width: 100%;
                                                border-radius: 5px;
                                                        height: 3em;
                                                                background-color: #2e7bcf;
                                                                        color: white;
                                                                            }
                                                                                </style>
                                                                                    """, unsafe_allow_html=True)

st.title("Handwritten Digit Recognition")
st.write("Draw a digit (0-9) in the box below and let the AI predict it!")

# Load model
@st.cache_resource
def load_trained_model():
      model = get_model()
      if os.path.exists("mnist_cnn.pth"):
                model.load_state_dict(torch.load("mnist_cnn.pth", map_location=torch.device('cpu')))
            model.eval()
    return model

model = load_trained_model()

# Create a canvas component
canvas_result = st_canvas(
      fill_color="rgba(255, 165, 0, 0.3)",
      stroke_width=20,
      stroke_color="#FFFFFF",
      background_color="#000000",
      height=280,
      width=280,
      drawing_mode="freedraw",
      key="canvas",
)

if canvas_result.image_data is not None:
      img = Image.fromarray(canvas_result.image_data.astype('uint8')).convert('L')
    img = img.resize((28, 28))

    transform = transforms.Compose([
              transforms.ToTensor(),
              transforms.Normalize((0.1307,), (0.3081,))
    ])
    img_tensor = transform(img).unsqueeze(0)

    if st.button("Predict"):
              with torch.no_grad():
                            output = model(img_tensor)
                            prob = F.softmax(output, dim=1)
                            pred = torch.argmax(prob, dim=1).item()
                            confidence = prob[0][pred].item() * 100

              st.markdown(f"### Prediction: **{pred}**")
              st.progress(confidence / 100)
              st.write(f"Confidence: {confidence:.2f}%")

st.sidebar.markdown("""
## About
This is a professional-grade Digit Recognition app using a **Convolutional Neural Network (CNN)** built with PyTorch.

### Tech Stack
- **PyTorch** (Deep Learning)
- **Streamlit** (Web Interface)
- **OpenCV/PIL** (Image Processing)
""")
