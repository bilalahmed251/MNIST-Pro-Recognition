<div align="center">

# 🖌️ MNIST Pro Recognition
### Professional Handwritten Digit Recognition System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/b098/mnist-pro-recognizer)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

**🎯 Draw any digit (0–9) and watch the CNN predict it in real time!**

[🚀 **Try the Live Demo**](https://huggingface.co/spaces/b098/mnist-pro-recognizer) · [📁 **View Code**](https://github.com/bilalahmed251/MNIST-Pro-Recognition) · [🐞 **Report Bug**](https://github.com/bilalahmed251/MNIST-Pro-Recognition/issues)

</div>

---

## 📌 Overview

A **production-ready** Handwritten Digit Recognition system powered by a custom **Convolutional Neural Network (CNN)** trained on the MNIST dataset. The project features a beautiful interactive **Streamlit** web app where users can draw digits freehand and receive instant AI predictions with confidence scores.

> ⚡ **Live on Hugging Face Spaces** → [https://huggingface.co/spaces/b098/mnist-pro-recognizer](https://huggingface.co/spaces/b098/mnist-pro-recognizer)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **CNN Architecture** | Multi-layer Conv2D → MaxPool → Dropout → Fully Connected |
| 🖌️ **Interactive Canvas** | Draw digits directly in the browser using a smooth freehand canvas |
| ⚡ **Real-time Inference** | Instant predictions with < 100ms latency on CPU |
| 📊 **Confidence Scores** | Visual progress bar showing prediction confidence (0–100%) |
| 🎨 **Dark UI** | Premium dark-themed Streamlit interface |
| ☁️ **Cloud Deployed** | Live on Hugging Face Spaces — no installation needed |

---

## 🛠️ Tech Stack

```
🧠 Deep Learning    →  PyTorch 2.2 (CPU-optimized)
🌐 Web Interface    →  Streamlit 1.32
🖼️ Image Processing →  PIL (Pillow), NumPy
🐳 Deployment       →  Docker + Hugging Face Spaces
📦 Data             →  MNIST Dataset (torchvision)
```

---

## 🧬 Model Architecture

```
Input (1×28×28)
     │
     ▼
Conv2D(1→32, 3×3) + ReLU
     │
MaxPool2D(2×2)
     │
Conv2D(32→64, 3×3) + ReLU
     │
MaxPool2D(2×2)
     │
Dropout(0.25)
     │
Flatten → FC(9216→128) + ReLU
     │
Dropout(0.5)
     │
FC(128→10) → Softmax
     │
Output (10 classes: 0–9)
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/bilalahmed251/MNIST-Pro-Recognition.git
cd MNIST-Pro-Recognition
```

### 2. Install Dependencies
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install streamlit streamlit-drawable-canvas numpy pillow
```

### 3. Train the Model
```bash
python train.py
```

### 4. Run the App Locally
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
MNIST-Pro-Recognition/
│
├── app.py              # 🌐 Streamlit web application
├── model.py            # 🧠 CNN model definition
├── train.py            # 🏋️ Model training script
├── requirements.txt    # 📦 Python dependencies
├── Dockerfile          # 🐳 Docker container config
└── README.md           # 📖 This file
```

---

## 🌐 Live Demo

👉 **[https://huggingface.co/spaces/b098/mnist-pro-recognizer](https://huggingface.co/spaces/b098/mnist-pro-recognizer)**

### How to use:
1. Open the live demo link above
2. **Draw** any digit (0–9) on the black canvas
3. Click **Predict**
4. See the AI's prediction + confidence score instantly!

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Dataset | MNIST (60K train / 10K test) |
| Test Accuracy | ~99% |
| Inference Speed | < 100ms (CPU) |
| Model Size | ~1.7 MB |
| Parameters | ~431K |

---

## 👨‍💻 Author

<div align="center">

**Bilal Ahmed**

[![GitHub](https://img.shields.io/badge/GitHub-bilalahmed251-181717?style=for-the-badge&logo=github)](https://github.com/bilalahmed251)
[![Hugging Face](https://img.shields.io/badge/🤗-b098-FFD21E?style=for-the-badge)](https://huggingface.co/b098)

*AI/ML Engineer · Computer Vision · NLP*

</div>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<div align="center">

⭐ **If you found this helpful, please give the repo a star!** ⭐

Made with ❤️ by [Bilal Ahmed](https://github.com/bilalahmed251)

</div>
