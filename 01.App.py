from flask import Flask, render_template, jsonify
import psutil
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    uptime = time.time() - psutil.boot_time()

    return jsonify({
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "uptime": round(uptime, 2)
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
