from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests
import os

app = Flask(__name__)

IPINFO_ACCESS_TOKEN = os.getenv('IPINFO_ACCESS_TOKEN')

def getClientAddressData(ipAddress):
    try:
        response = requests.get(f'https://ipinfo.io/{ipAddress}/json?token={IPINFO_ACCESS_TOKEN}')
        ipInfo = response.json()
    except requests.RequestException:
        ipInfo = "Error fetching address info"
    return ipInfo

def createImageWithText(text, imageSize=(1000, 500)):
    image = Image.new('RGB', imageSize, color='black')
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf")
    except IOError:
        font = ImageFont.load_default(11)
        print("Default font loaded.")
    position = (20, 20)
    draw.text(position, text, fill="white", font=font)
    
    return image

@app.route("/")
def home():
    location_info = [f"{key.capitalize()}: {value}" for key, value in getClientAddressData(request.remote_addr).items()]
    request_data = [
        f"Method: {request.method}",
        f"URL: {request.url}",
        "Headers:",
        *[f"{key}: {value}" for key, value in request.headers.items()],
        "Args:",
        *[f"{key}: {value}" for key, value in request.args.items()],
        # Include additional sections for Form, Data, Json, Cookies as needed
        f"Remote Addr: {request.remote_addr}",
        f"User Agent: {request.user_agent.string}",
        *location_info,
        f"Real IP: {request.headers.get('X-Forwarded-For', request.remote_addr)}"
    ]
    imageText = "\n".join(request_data)
    
    # Create an image with the IP address text
    image = createImageWithText(imageText)
    
    # Prepare the image for sending by saving to a BytesIO buffer
    img_io = BytesIO()
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    
    # Send the image as a response
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=4000)