from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('indexMultiLanguage.html')  # Render the page with the WebSocket code

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    # You can handle further processing of the received text here
    socketio.emit('response', {'data': message})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)