from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from sense_hat import SenseHat

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins

sense = SenseHat()

# -----------------------------
# SENSOR FUNCTIONS
# -----------------------------

def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            cpu_temp = float(f.read()) / 1000.0
        return cpu_temp
    except:
        return 0.0

def set_led_alert(temp, humidity, pressure):
    color = (0, 255, 0)  # Green by default

    if temp < 15 or temp > 30 or humidity < 10 or pressure < 800:
        color = (255, 0, 0)  # Red
    elif temp < 18 or temp > 28 or humidity < 5 or pressure < 850:
        color = (255, 255, 0)  # Yellow

    sense.clear(color)

# -----------------------------
# ROUTES
# -----------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    """Optional: Returns current sensor data in JSON."""
    try:
        room_temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        cpu_temp = get_cpu_temperature()
        adjusted_temp = room_temp - (cpu_temp - room_temp)

        set_led_alert(adjusted_temp, humidity, pressure)

        return jsonify({
            "temperature": round(adjusted_temp, 1),
            "humidity": round(humidity, 1),
            "pressure": round(pressure, 1)
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# -----------------------------
# BACKGROUND TASK FOR SOCKET.IO
# -----------------------------

def sensor_loop():
    """Send sensor data to all clients every second."""
    while True:
        try:
            room_temp = sense.get_temperature()
            humidity = sense.get_humidity()
            pressure = sense.get_pressure()
            cpu_temp = get_cpu_temperature()
            adjusted_temp = room_temp - (cpu_temp - room_temp)

            set_led_alert(adjusted_temp, humidity, pressure)

            # Emit data to all connected clients
            socketio.emit("sensorUpdate", {
                "temperature": round(adjusted_temp, 1),
                "humidity": round(humidity, 1),
                "pressure": round(pressure, 1)
            })

        except Exception as e:
            print("Sensor loop error:", e)

        socketio.sleep(1)  # non-blocking sleep

# Start background task
socketio.start_background_task(sensor_loop)

# -----------------------------
# MAIN
# -----------------------------

if __name__ == '__main__':
    # host='0.0.0.0' allows access from other devices in your LAN
    socketio.run(app, host='0.0.0.0', port=5000)
