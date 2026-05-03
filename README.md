# 🚀 Professional Handwritten Digit Recognition

![Project Banner](assets/banner.png)

## 🌟 Featured Project
A state-of-the-art Handwritten Digit Recognition system leveraging a multi-class Convolutional Neural Network (CNN) built with PyTorch. This project features a real-time interactive Streamlit web application where users can draw digits and get instant predictions.

### 🧠 Algorithm: Convolutional Neural Network (CNN)
To achieve high accuracy on the MNIST dataset, I implemented a deep CNN architecture.
- **Feature Extraction**: Multiple convolutional layers with ReLU activation to capture spatial hierarchies in digit strokes.
- **Pooling**: Max-pooling layers to reduce spatial dimensions and ensure translation invariance.
- **Classification**: Fully connected layers with LogSoftmax for precise multi-class probability distribution.

### 🛠️ Technical Workflow
1. **Data Preprocessing**: Normalized MNIST images to a standard range and applied data augmentation for better generalization.
2. **Model Training**: Trained the CNN using Negative Log Likelihood Loss (NLLLoss) and the Adam optimizer.
3. **Interactive Interface**: Developed a Streamlit dashboard with `streamlit-drawable-canvas` for real-time user interaction.
4. **Model Deployment**: Integrated the PyTorch model into the web app for on-the-fly inference.

### 💻 Tech Stack
- **Deep Learning**: PyTorch
- **Web Framework**: Streamlit
- **Data Science**: NumPy, Matplotlib
- **Computer Vision**: OpenCV, PIL
