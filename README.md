

# Mini Voice AI Assistant


## Description
A simple, privacy-friendly voice AI assistant that listens to you, understands your question, and replies with speech. Powered by local LLMs (Ollama) and Google Speech-to-Text/Text-to-Speech. Use via CLI or a modern web interface.

---


## Features
- 🎤 Record audio from your microphone (CLI or web)
- 📝 Transcribe speech to text (Google STT)
- 🤖 Get smart answers from a local LLM (Ollama, e.g., Llama 3)
- 🔊 Convert the response to speech (gTTS)
- ▶️ Play the audio reply
- 🌐 Simple web UI with Record button and playback controls
- 💻 CLI interface for terminal lovers

---

## Quick Start


### 1. Clone the repository
```bash
git clone https://github.com/Alireza-Mahinparvar/vapi-ai
cd vapi-ai/vapi-ai
```


### 2. Set up Python environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```


### 3. Install dependencies
```bash
pip install -r requirements.txt
```



### 4. Install Ollama (for local LLM)
Ollama is required to run the local LLM (e.g., Llama 3). You need to run Ollama in a separate terminal window before starting the web or CLI app.

**Step 1: Open a new terminal window and run Ollama server:**
```bash
brew install ollama
ollama serve
```

**Step 2: In the same terminal, pull the Llama 3 model:**
```bash
ollama pull llama3
```

**You should always keep the Ollama server running in one terminal.**

**In a second terminal, activate your Python environment and run the app as described below.**


### 5. (Optional) Install ffmpeg for web audio support
```bash
brew install ffmpeg
```


### 6. Run the CLI assistant
```bash
python main.py
```


### 7. Run the web app
```bash
python app.py
# Then open http://localhost:5000 in your browser
```

---

## Usage

**CLI:**
- Follow the prompts to record your question and hear the AI’s spoken reply.
- Say or type "goodbye" to end the conversation.


**Web:**
- Click the Record button, speak, and wait for the AI’s spoken reply.

---


## Demo
Add a GIF, video, or audio clip of the bot in action here!

---


## Requirements
- Python 3.8+
- macOS (for afplay audio playback)
- Microphone and speakers
- Ollama (for local LLM)
- ffmpeg (for web audio conversion)
- All Python dependencies in `requirements.txt` (see below)

### Python dependencies (requirements.txt)
```
flask
soundfile
numpy
gtts
openai
SpeechRecognition
sounddevice
playsound
```

---


## License
MIT
