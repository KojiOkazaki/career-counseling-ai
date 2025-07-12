# 🤖 Career Counseling Evaluation AI

This is a web application that uses AI to evaluate a recording of a career counseling session. You can upload an audio file (like M4A or MP3), and the tool will provide a structured evaluation and suggestions for improvement based on professional counseling criteria.

The application uses **OpenAI's Whisper** for transcription and **GPT-4o** for evaluation.

![Screenshot of the app](<YOUR_SCREENSHOT_URL_HERE>)  ---

## ⚠️ Important Privacy Notice

This application sends the transcribed text from your audio file to the OpenAI API for analysis.

-   **DO NOT** upload audio containing sensitive personal information (names, addresses, financial details, etc.).
-   By using this tool, you acknowledge that your data is processed by a third-party service.

---

## 🚀 Getting Started

Follow these steps to run the application on your own computer.

### Prerequisites

-   Python 3.8 or newer
-   [FFmpeg](https://ffmpeg.org/download.html) (This is required by Whisper to process different audio formats). Please install it and ensure it's accessible in your system's PATH.

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/career-counseling-ai.git
    cd career-counseling-ai
    ```

2.  **Create a Virtual Environment (Recommended)**
    This keeps the project's dependencies isolated from other Python projects.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    This command installs all the necessary Python packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Your API Key**
    The application needs an OpenAI API key to work.
    
    -   Create a file named `.env` in the project's main directory.
    -   Add your API key to this file like so:
        ```
        OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```
    *This `.env` file is listed in `.gitignore`, so it will **never** be uploaded to GitHub.*

### How to Run the App

With your virtual environment activated and your `.env` file set up, run the following command:

```bash
python app.py
```

A message will appear in your terminal with a local URL (usually `http://127.0.0.1:7860`). Open this URL in your web browser to use the application.

---

## How to Use

1.  Open the application in your browser.
2.  Click or drag your audio file (e.g., `.m4a`, `.mp3`, `.wav`) into the upload box.
3.  Click the **Submit** button.
4.  Wait a few moments for the transcription and AI evaluation.
5.  The evaluation will appear in the "Evaluation Result" box on the right.
