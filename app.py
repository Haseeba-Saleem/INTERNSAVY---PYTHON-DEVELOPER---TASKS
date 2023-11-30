from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('message', {'username': 'System', 'message': f'{data["username"]} has joined the room.'}, room=room, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
