# AI Image Summarizer 🔍

A streamlined, AI-powered application that generates detailed descriptions and concise summaries of your images using local Vision-Language Models (VLM).

**Demo Video:** [Demo Video]

[Demo Video]: https://drive.google.com/file/d/1HsgLAybTEJ7LesrBYcNMOpCXKTaFkuLr/view?usp=sharing

---

## 🚀 Features

* **Instant Analysis** – Automatically generates both a detailed description and a quick summary upon upload.
* **Privacy-Focused** – Runs entirely locally on your machine using Ollama.
* **Clean UI** – Minimalist, distraction-free interface built with Streamlit.
* **Dual Output**

  * 📝 **Description** – A comprehensive breakdown of the image content
  * 💡 **Summary** – A bullet-point overview for quick digesting

---

## 🛠️ Prerequisites

* **Ollama**
  You need Ollama installed and running on your system.

* **Python 3.8+**
  Ensure you have a compatible Python version installed.

---

## 📥 Installation

### 1. Clone or download this repository

Clone or download this repository to your local machine.

---

### 2. Install Ollama

Download and install Ollama from:

[https://ollama.ai](https://ollama.ai)

Make sure it is running:

```bash
ollama serve
```

(or start it from the system tray).

---

### 3. Pull the required model

This application uses the **llava:13b** model for high-quality image analysis.

```bash
ollama pull llava:13b
```

**Note**

* Model size is ~8GB
* At least **16GB RAM** is recommended for smooth performance

---

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 🎮 How to Run

### 1. Start the application

```bash
streamlit run app.py
```

(Or use the provided `run.bat` file if you are on Windows.)

---

### 2. Use the app

* The application opens in your browser (usually `http://localhost:8501`)
* Upload an image (PNG / JPG / JPEG)
* The model automatically analyzes the image
* View:

  * detailed description
  * short summary
* Click refresh to clear and analyze another image

---

## 🧩 Tech Stack

* **Frontend** – Streamlit
* **AI Backend** – Ollama
* **Model** – LLaVA 13B (Large Language-and-Vision Assistant)
* **Language** – Python
