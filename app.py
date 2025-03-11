from flask import Flask
import os

app = Flask(__name__)

# Read environment variables
MONGO_IP = os.getenv("Mongoip", "localhost")
MONGO_PORT = os.getenv("Mongoport", "27017")
DEV_MODE = os.getenv("Dev", "true")
MONGO_PASSWORD = os.getenv("Mongopassword", "password")
DEBUG_MODE = os.getenv("Debug", "false")
SERVICE_NAME = os.getenv("Service_name", "my-app")
MONGO_DB = os.getenv("MongoDB", "mydatabase")

@app.route('/')
def home():
    return f"Hello from {SERVICE_NAME}! MongoDB at {MONGO_IP}:{MONGO_PORT}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8189, debug=DEBUG_MODE.lower() == "true")
