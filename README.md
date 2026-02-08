# AI Image Summarizer 🔍

A streamlined, AI-powered application that generates detailed descriptions and concise summaries of your images using local Vision-Language Models (VLM).

## 🚀 Features

- **Instant Analysis**: Automatically generates both a detailed description and a quick summary upon upload.
- **Privacy-Focused**: Runs entirely locally on your machine using Ollama.
- **Clean UI**: Minimalist, distraction-free interface built with Streamlit.
- **Dual Output**: 
  - 📝 **Description**: A comprehensive breakdown of the image content.
  - 💡 **Summary**: A bullet-point overview for quick digesting.

## 🛠️ Prerequisites

- **Ollama**: You need [Ollama](https://ollama.ai) installed and running on your system.
- **Python 3.8+**: Ensure you have a compatible Python version installed.

## 📥 Installation

1.  **Clone/Download this repository** to your local machine.

2.  **Install Ollama** (if not already installed):
    *   Download from [ollama.ai](https://ollama.ai).
    *   Install and ensure it is running (`ollama serve` or via system tray).

3.  **Pull the Required Model**:
    *   This application uses the `llava:13b` model for high-quality image analysis.
    *   Open your terminal/command prompt and run:
        ```bash
        ollama pull llava:13b
        ```
    *   *Note: This model is approximately 8GB. Ensure you have enough disk space and at least 16GB of RAM is recommended for smooth performance.*

4.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🎮 How to Run

1.  **Start the Application**:
    ```bash
    streamlit run app.py
    ```
    *Or use the provided `run.bat` file if on Windows.*

2.  **Use the App**:
    *   The application will open in your default web browser (usually http://localhost:8501).
    *   **Upload an Image**: Drag and drop or click to select a PNG, JPG, or JPEG file.
    *   **Wait for Analysis**: The AI will automatically process the image.
    *   **View Results**: Read the detailed description and summary below the image.
    *   **Analyze Another**: Click the refresh button to clear and start over.

## 🧩 Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **AI Backend**: [Ollama](https://ollama.ai/)
-   **Model**: LLaVA 13B (Large Language-and-Vision Assistant)
-   **Language**: Python


