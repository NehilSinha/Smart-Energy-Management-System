from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import datetime
import sqlite3
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
CORS(app)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('devices.db')
    conn.row_factory = sqlite3.Row
    return conn


# Create the devices table if it doesn't exist
def init_db():
    conn = get_db_connection()
    # Create the devices table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY,
            name TEXT,
            status TEXT,
            power_consumption REAL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS device_history (
            device_id INTEGER,
            date TEXT,
            power_consumption REAL,
            FOREIGN KEY (device_id) REFERENCES devices (id)
        )
    ''')

    # Insert initial devices if they don't already exist
    devices = conn.execute('SELECT * FROM devices').fetchall()
    if len(devices) == 0:  # If no devices exist, insert some sample devices
        conn.execute('INSERT INTO devices (name, status, power_consumption) VALUES (?, ?, ?)',
                     ("Smart Plug 1", "off", 0))
        conn.execute('INSERT INTO devices (name, status, power_consumption) VALUES (?, ?, ?)',
                     ("Smart Plug 2", "off", 0))
        conn.commit()

    conn.close()

init_db()


# Endpoint to get energy consumption data
@app.route('/api/devices', methods=['GET'])
def get_devices():
    conn = get_db_connection()
    devices = conn.execute('SELECT * FROM devices').fetchall()
    conn.close()

    devices_data = []
    for device in devices:
        devices_data.append({
            "id": device["id"],
            "name": device["name"],
            "status": device["status"],
            "power_consumption": device["power_consumption"]
        })
    return jsonify({"devices": devices_data})


# Endpoint to toggle device status
@app.route('/api/device/<int:device_id>/toggle', methods=['POST'])
def toggle_device(device_id):
    conn = get_db_connection()
    device = conn.execute('SELECT * FROM devices WHERE id = ?', (device_id,)).fetchone()

    if not device:
        return jsonify({"error": "Device not found"}), 404

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    power_consumption = random.uniform(1, 10)

    if device["status"] == "off":
        conn.execute('UPDATE devices SET status = ?, power_consumption = ? WHERE id = ?',
                     ('on', power_consumption, device_id))
        conn.execute('INSERT INTO device_history (device_id, date, power_consumption) VALUES (?, ?, ?)',
                     (device_id, today, power_consumption))
    else:
        conn.execute('UPDATE devices SET status = ?, power_consumption = ? WHERE id = ?',
                     ('off', 0, device_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Device toggled successfully"})


# Endpoint to get power consumption history
@app.route('/api/device/history', methods=['GET'])
def get_all_device_history():
    conn = get_db_connection()

    # Fetch all devices
    devices = conn.execute('SELECT * FROM devices').fetchall()

    all_history = []

    # Loop through each device and fetch its history
    for device in devices:
        device_id = device["id"]
        history = conn.execute('SELECT * FROM device_history WHERE device_id = ?', (device_id,)).fetchall()

        history_data = []
        for entry in history:
            history_data.append({
                "date": entry["date"],
                "power_consumption": entry["power_consumption"]
            })

        if history_data:
            all_history.append({
                "device_id": device_id,
                "name": device["name"],
                "history": history_data
            })

    conn.close()

    # If no history data found
    if not all_history:
        return jsonify({"error": "No history data available for any device"}), 404

    return jsonify({"devices": all_history})


# ML Analysis and Automatic Control
@app.route('/api/analyze-and-turn-off', methods=['POST'])
def analyze_and_turn_off():
    conn = get_db_connection()
    devices = conn.execute('SELECT * FROM devices').fetchall()

    results = []
    IDLE_THRESHOLD = 5  # Example threshold in watts
    for device in devices:
        device_id = device["id"]
        history = conn.execute('SELECT * FROM device_history WHERE device_id = ?', (device_id,)).fetchall()

        if not history:
            continue  # Skip if there's no history

        # Prepare data for ML model: we are using the last 10 data points to predict the idle state
        power_consumptions = [entry["power_consumption"] for entry in history]
        if len(power_consumptions) < 2:
            continue  # We need at least two data points to predict

        # Train a linear regression model
        X = np.array(range(len(power_consumptions))).reshape(-1, 1)
        y = np.array(power_consumptions)
        model = LinearRegression()
        model.fit(X, y)

        # Predict the next power consumption
        prediction = model.predict([[len(power_consumptions)]])
        avg_consumption = prediction[0]

        # Check if the device is idle
        if avg_consumption < IDLE_THRESHOLD and device["status"] == "on":
            conn.execute('UPDATE devices SET status = ?, power_consumption = ? WHERE id = ?',
                         ('off', 0, device_id))
            results.append({"device_id": device_id, "turned_off": True})
        else:
            results.append({"device_id": device_id, "turned_off": False})

    conn.commit()
    conn.close()

    return jsonify({"results": results})


if __name__ == '__main__':
    app.run(debug=True)
