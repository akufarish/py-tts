from flask import Flask, render_template, request, send_file
from gtts import gTTS
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def post_tts():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            tts = gTTS(text, lang='id')
            tts.save('tts.mp3')
            return send_file('tts.mp3', as_attachment=True)
    return render_template('index.html')