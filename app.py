from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory logs (can be replaced with database)
qr_logs = []
bluetooth_logs = []

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")


# API: Log QR scan
@app.route("/api/qr-scan", methods=["POST"])
def qr_scan():
    data = request.json
    log = {
        "data": data.get("qrData"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    qr_logs.append(log)
    return jsonify({"status": "QR scan logged"})


# API: Log Bluetooth device
@app.route("/api/bluetooth", methods=["POST"])
def bluetooth_log():
    data = request.json
    log = {
        "device": data.get("deviceName"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    bluetooth_logs.append(log)
    return jsonify({"status": "Bluetooth device logged"})


# API: View logs (for testing/admin)
@app.route("/api/logs")
def logs():
    return jsonify({
        "qr_logs": qr_logs,
        "bluetooth_logs": bluetooth_logs
    })


if __name__ == "__main__":
    app.run(debug=True)
