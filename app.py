from flask import Flask, render_template, request, send_file, jsonify
import tempfile
import os
from main import transcribe_audio, ask_llm, speak_text, save_wav
import soundfile as sf
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Receive audio file from frontend
    audio_file = request.files['audio']
    with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_in:
        audio_file.save(temp_in.name)
        # Convert to PCM WAV using ffmpeg
        temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_wav.close()
        ffmpeg_cmd = f"ffmpeg -y -i {temp_in.name} -ar 16000 -ac 1 -f wav {temp_wav.name}"
        os.system(ffmpeg_cmd)
        text = transcribe_audio(temp_wav.name)
        os.remove(temp_in.name)
        os.remove(temp_wav.name)
    if not text:
        return jsonify({'error': 'Could not transcribe audio.'}), 400
    answer = ask_llm(text)
    # Synthesize answer to speech
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_tts:
        from gtts import gTTS
        tts = gTTS(text=answer, lang='en')
        tts.save(temp_tts.name)
        mp3_path = temp_tts.name
    return send_file(mp3_path, mimetype='audio/mpeg', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
