from flask import Flask
from threading import Thread
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is alive!"

def find_available_port(start_port=8080, max_retries=10):
    """Find an available port starting from `start_port`."""
    for i in range(max_retries):
        port = start_port + i
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('0.0.0.0', port))
            if result != 0:
                return port
    raise Exception(f"Unable to find an available port after {max_retries} retries")

def run():
    """Run the Flask app with a dynamically assigned available port."""
    port = find_available_port()  # Find an available port starting from 8080
    print(f"Starting server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

def keep_alive():
    """Run the Flask app in a separate thread to keep it alive."""
    t = Thread(target=run)
    t.start()
