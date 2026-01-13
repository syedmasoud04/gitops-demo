from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Kubernetes! Version: {os.environ.get('VERSION', '1.0.0')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
