import cv2
import numpy as np


def load_reference(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (32, 32))
    return img.flatten()


ARDUINO_REF = load_reference(
    "TinyDB/Arduino-Uno/arduino.jpg"
)

SOIL_REF = load_reference(
    "TinyDB/Soil-Moisture-Sensor/soil.jpg"
)


def compare_image(captured, reference):
    diff = np.sum(
        np.abs(
            captured.astype(np.int32)
            -
            reference.astype(np.int32)
        )
    )

    return diff


def recognize_component(image_path):

    img = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    img = cv2.resize(
        img,
        (32, 32)
    )

    captured = img.flatten()

    score_arduino = compare_image(
        captured,
        ARDUINO_REF
    )

    score_soil = compare_image(
        captured,
        SOIL_REF
    )

    if score_arduino < score_soil:
        detected = "Arduino-Uno"
        best = score_arduino
        worst = score_soil

    else:
        detected = "Soil-Moisture-Sensor"
        best = score_soil
        worst = score_arduino

    confidence = max(
        0,
        round(
            100 -
            ((best / worst) * 100),
            2
        )
    )

    return {
        "component": detected,
        "confidence": float(confidence)
    }