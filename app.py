from flask import Flask, render_template, request, jsonify

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
    return jsonify(status="success", latitude=latitude, longitude=longitude)

if __name__ == '__main__':
    app.run(debug=True)
