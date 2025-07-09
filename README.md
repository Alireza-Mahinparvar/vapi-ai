# Mini Voice AI Assistant

## Description
A simple voice AI that listens to you, understands your question, and replies with speech. Built in one day using Python.

## Features
- Record audio from your microphone
- Transcribe speech to text
- Send text to an LLM (OpenAI GPT-3.5/4 or Gemini)
- Convert the response text to speech
- Play the audio reply
- Simple CLI interface

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd voice_ai_assistant
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**
   - Export your key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run the assistant**
   ```bash
   python main.py
   ```

## Usage Example
- Run the script and follow the CLI prompts to record your question and hear the AI's spoken reply.

## Demo
- (Add your demo audio/video/gif here)

## Requirements
- Python 3.8+
- Microphone and speakers

## License
MIT
