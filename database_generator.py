import cv2

def image_to_array(image_path):
    img = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    img = cv2.resize(
        img,
        (32, 32)
    )

    flat = img.flatten()

    print(
        "const uint8_t IMAGE[1024] PROGMEM={"
    )

    for i, v in enumerate(flat):
        print(v, end=",")

        if i % 20 == 0:
            print()

    print("};")


image_to_array(
    "TinyDB/Soil-Moisture-Sensor/soil.jpg"
)