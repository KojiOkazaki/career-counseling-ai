import os
import openai
import whisper
import gradio as gr
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Step 1: Load API Key and Initialize Clients ---
# Load environment variables from a .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize the OpenAI client (using the new openai > 1.0.0 syntax)
try:
    client = openai.OpenAI(api_key=api_key)
except Exception as e:
    logging.error(f"Failed to initialize OpenAI client: {e}")
    raise

# --- Step 2: Load the Whisper Model Once ---
# Load the model on startup, not every time the function is called.
try:
    whisper_model = whisper.load_model("base")
    logging.info("Whisper model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load Whisper model: {e}")
    raise

# --- Step 3: Define Core Functions ---
def evaluate_counseling_session(transcribed_text):
    """Sends transcribed text to GPT-4o for evaluation."""
    system_prompt = "You are a professional career counseling evaluator. Your analysis should be constructive, clear, and structured using Markdown."
    user_prompt = f"""
    Please evaluate the following career counseling session transcript.

    **Evaluation Criteria:**
    1.  **Counseling Purpose:** Was a clear goal set for the session?
    2.  **Communication Quality:** Was communication bilateral and empathetic?
    3.  **Use of Theories/Tools:** Were specific career theories or tools applied?
    4.  **Client Self-Understanding:** Was the client's self-understanding promoted?
    5.  **Decision-Making Support:** Was the client supported in their decision-making process?

    **Transcript:**
    ---
    {transcribed_text}
    ---

    **Instructions:**
    Provide a concise evaluation for each criterion, followed by specific, actionable advice for improvement. If the provided audio doesn't seem to be a counseling session, please state that first. Format your entire response using Markdown.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error calling OpenAI API: {e}")
        return "Error: Could not get an evaluation from the AI. Please check the logs."

def process_audio(audio_filepath):
    """Transcribes audio and sends it for evaluation."""
    if audio_filepath is None:
        return "Please upload an audio file first."

    logging.info(f"Processing audio file: {audio_filepath}")
    
    try:
        # Transcribe audio
        transcription_result = whisper_model.transcribe(audio_filepath, fp16=False)
        transcribed_text = transcription_result["text"]
        logging.info("Transcription complete.")
        
        if not transcribed_text.strip():
            return "The audio appears to be empty or silent. No text was transcribed."

        # Get evaluation
        evaluation_result = evaluate_counseling_session(transcribed_text)
        logging.info("Evaluation complete.")
        
        return evaluation_result
    
    except Exception as e:
        logging.error(f"An error occurred during audio processing: {e}")
        return "An error occurred. Please ensure you have a valid audio file and try again."
    finally:
        # Clean up the temporary file Gradio creates
        if audio_filepath and os.path.exists(audio_filepath):
            os.remove(audio_filepath)
            logging.info(f"Cleaned up temporary file: {audio_filepath}")


# --- Step 4: Create Gradio Interface ---
# Added a more detailed description and a privacy disclaimer.
description = """
### Upload an M4A or MP3 audio file of a career counseling session.
The AI will transcribe the session and provide an evaluation with advice for improvement.

**⚠️ Privacy Disclaimer:**
Your audio is transcribed and the text is sent to a third-party AI (OpenAI) for analysis. **Do not upload audio containing sensitive personal or confidential information.** By using this service, you acknowledge and accept this.
"""

gr_interface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Upload Audio File (m4a, mp3, wav...)"),
    outputs=gr.Markdown(label="Evaluation Result", sanitize_html=False),
    title="🤖 Career Counseling Evaluation AI",
    description=description,
    allow_flagging="never", # Disables the "Flag" button
)

# --- Step 5: Launch the App ---
if __name__ == "__main__":
    gr_interface.launch()
