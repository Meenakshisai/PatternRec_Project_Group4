# PatternRec_Project_Group4
# 🍇 Blackberry & Lime Visual Classifier

This is the final project submission for **CSE 455/555 – Intro to Pattern Recognition and Deep Learning**, University at Buffalo.

---

## 📌 Project Overview

We built an end-to-end image classification system to:

- 🥝 Identify whether the input fruit is a **blackberry** or a **lime**
- 🧺 Determine how the fruit is presented: e.g. Halved, In a Container, Whole, etc.

The app uses **transfer learning** via pre-trained **ResNet-18**, and is deployed as a live web app using **Gradio on Hugging Face Spaces**.

---

## 📂 Dataset

- ✅ Collected manually
- 🎯 2 produce categories:
  - **blackberry**
  - **lime**
- 🎯 6 variation categories:
  - Halved
  - In Context
  - In a Container
  - Single Berry
  - Small Group
  - Whole

Total images: ~1800  
Split: 70% Train, 20% Validation, 10% Test

---

## 🧠 Model

- Base Model: `ResNet-18` (pretrained on ImageNet)
- Two-stage classifiers:
  - `produce_classifier.pth` – blackberry vs lime
  - `variation_classifier.pth` – 6-class variation
- Frozen all layers except the final classification head
- Optimizer: `Adam`
- Loss: `CrossEntropyLoss`
- Epochs: `5`

---

## 📊 Performance

### 🍇 Produce Classifier

- Accuracy: **100%**
- Precision, Recall, F1-score: **1.00** for both classes

### 🧺 Variation Classifier

- Accuracy: **99%**
- Macro & Weighted F1-score: **0.99**

---

## 🌐 Web App Demo

🧪 Try the live web app:

👉 **Hugging Face Space:**  
[https://huggingface.co/spaces/brs13/blackberry-lime-classifier](https://huggingface.co/spaces/brs13/blackberry-lime-classifier)

### 🔍 How to Use the App

1. Click the link above to launch the app.
2. Upload a fruit image (blackberry or lime).
3. The app will:
   - Predict the produce type (blackberry or lime).
   - Predict its visual presentation category (e.g., Whole, Halved).
4. You will also see example images and model outputs.

---

## 📄 How to View the Project Report (index.html)

This project includes a detailed and self-contained **HTML report** summarizing everything we did.

#### 🧾 Steps to View:

1. **Clone or download** this GitHub repository to your computer.
2. Locate the file named `index.html` in the root directory.
3. **Double-click** the file to open it in any modern web browser (e.g., Chrome, Firefox, Safari).
4. The report contains:
   - ✅ Full project description  
   - 📊 Confusion matrices and performance results  
   - 🧠 Model details and training setup  
   - 🚀 Summary, future work, and app links
---
