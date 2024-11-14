from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menerima data GPS dari klien
@app.route('/gps', methods=['POST'])
def get_gps():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = data.get('timestamp')  # Mendapatkan timestamp dari klien

    # Menyimpan data GPS dan waktu akses ke file log
    with open("gps_log.txt", "a") as log_file:
        log_entry = f"Accessed at {timestamp}, Latitude: {latitude}, Longitude: {longitude}\n"
        log_file.write(log_entry)

    return jsonify(status="success", latitude=latitude, longitude=longitude, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
