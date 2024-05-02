import numpy as np
import base64
import cv2

def url_to_image(data_url):
    # Extract base64 data from the data URL
    header, base64_data = data_url.split(',', 1)
    image_data = base64.b64decode(base64_data)
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

def process_url(data):
    imageURL = data['dataUrl']
    timestamp = data['timestamp']
    sNo = data['serialNumber']
    if imageURL:
        print(sNo)
        image = url_to_image(imageURL)
        save_path = r'frames/{}.jpg'.format(timestamp)
        cv2.imwrite(save_path, image)
