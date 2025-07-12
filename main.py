import os
import requests
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from gtts import gTTS
import tempfile
import subprocess
import wave

# Record voice from microphone
def record_voice(duration=5, fs=16000):
    print("Talk now...")
    voice = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Recording done")
    return np.squeeze(voice)

# Save voice to WAV
def save_wav(voice, fs, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(fs)
        wf.writeframes(voice.tobytes())

# Transcribe WAV voice to text using Google STT
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        voice = recognizer.record(source)
    try:
        text = recognizer.recognize_google(voice)
        print(f"You said: {text}")
        return text
    except Exception as e:
        print(" Could not transcribe voice:", e)
        return None

# Ask local Ollama LLM (e.g., llama3)
def ask_llm(prompt, model="llama3"):
    print("waiting ...")
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    try:
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        # Handle both streaming and non-streaming JSON responses
        try:
            data = resp.json()
            answer = data["message"]["content"].strip()
        except Exception:
            # If multiple JSON objects, get the first one
            lines = resp.text.strip().splitlines()
            for line in lines:
                if line.strip():
                    try:
                        data = requests.models.json.loads(line)
                        answer = data["message"]["content"].strip()
                        break
                    except Exception:
                        continue
            else:
                answer = "Sorry, I couldn't parse the response from the local AI."
        print(f"AI: {answer}")
        return answer
    except Exception as e:
        print("Ollama API error:", e)
        return "Sorry, I couldn't get a response from the local AI."

# Speak text using gTTS + afplay (macOS)
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        subprocess.run(['afplay', fp.name])  # macOS voice player
    os.remove(fp.name)

# Main loop
def main():
    fs = 16000
    duration = 5  # seconds

    print("Type 'goodbye' or say 'goodbye' to end the conversation.")
    while True:
        voice = record_voice(duration, fs)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as fp:
            save_wav(voice, fs, fp.name)
            text = transcribe_audio(fp.name)
        os.remove(fp.name)

        if not text:
            continue

        if 'goodbye' in text.lower():
            print(" Conversation closed.")
            speak_text("Goodbye!")
            break

        response = ask_llm(text)
        speak_text(response)

if __name__ == "__main__":
    main()
