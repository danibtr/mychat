from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, emit
from utils.translate import translate_message
from utils.auth import google_login

app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    user = session.get('user')
    if not user:
        return redirect('/')
    return render_template('chat.html', user=user)

@socketio.on('send_message')
def handle_message(data):
    translated = translate_message(data['message'])
    emit('receive_message', {'user': data['user'], 'message': translated}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
