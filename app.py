from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

import os

from recognition import recognize_component

app = Flask(__name__)

# Smart Farm State
state = {
    "Farm Brain": False,
    "Water Guardian": False
}


# Home Dashboard
@app.route("/")
def home():

    completion = 0

    if state["Farm Brain"]:
        completion += 50

    if state["Water Guardian"]:
        completion += 50

    return render_template(
        "index.html",
        farm_brain="Unlocked ✅" if state["Farm Brain"] else "Locked ❌",
        water_guardian="Unlocked ✅" if state["Water Guardian"] else "Locked ❌",
        completion=completion
    )


# Upload Page
@app.route("/upload")
def upload_page():
    return render_template("upload.html")


# Image Recognition Route
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    save_path = os.path.join(
        "test_images",
        image.filename
    )

    image.save(save_path)

    result = recognize_component(
        save_path
    )

    component = result["component"]

    # Unlock Assets
    if component == "Arduino-Uno":
        state["Farm Brain"] = True

    if component == "Soil-Moisture-Sensor":
        state["Water Guardian"] = True

    return jsonify(result)


# ESP32/API Update Route
@app.route("/update", methods=["POST"])
def update():

    data = request.json

    component = data.get("component")

    if component == "Arduino-Uno":
        state["Farm Brain"] = True

    if component == "Soil-Moisture-Sensor":
        state["Water Guardian"] = True

    return jsonify({
        "status": "success",
        "component": component
    })


# Optional Testing Routes
@app.route("/unlock_arduino")
def unlock_arduino():
    state["Farm Brain"] = True
    return "Arduino Uno Unlocked"


@app.route("/unlock_soil")
def unlock_soil():
    state["Water Guardian"] = True
    return "Soil Moisture Sensor Unlocked"


@app.route("/reset")
def reset():

    state["Farm Brain"] = False
    state["Water Guardian"] = False

    return "Dashboard Reset"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )