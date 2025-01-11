from flask import Flask, render_template, request, send_file
from gtts import gTTS
from io import BytesIO
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def post_tts():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            tts_fp = BytesIO()
            tts = gTTS(text, lang='id')
            tts.write_to_fp(tts_fp)
            tts_fp.seek(0)
            return send_file(tts_fp, mimetype='audio/mpeg', as_attachment=False)
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_tts():
    text = request.form['text']
    if text:
        tts_fp = BytesIO()
        tts = gTTS(text, lang='id')
        tts.write_to_fp(tts_fp)
        tts_fp.seek(0)
        return send_file(tts_fp, mimetype='audio/mpeg', as_attachment=True, download_name='tts.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)