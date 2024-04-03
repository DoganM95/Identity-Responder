from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def home():
    userIP = request.remote_addr
    imageText = "Your IP: {userIp}"

    return imageText

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)