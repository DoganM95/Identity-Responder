from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

def createImageWithText(text, imageSize=(300, 200), fontSize=11):
    image = Image.new('RGB', imageSize, color = 'black') # RGB image with 300x200 and backColor black
    draw = ImageDraw.Draw(image) # Create the image with given settings
    font = ImageFont.truetype("arial.ttf", fontSize) # Set font details
    textWidth, textHeight = draw.textsize(text, font=font) # Create text object with given settings
    position = ((imageSize[0]-textWidth)/2, (imageSize[1]-textHeight)/2) # Position text
    draw.text(position, text, fill="white", font=font) # Add white text on background image
    return image

@app.route("/")
def home():
    userIP = request.remote_addr
    imageText = "Your IP: {userIp}"
    image = createImageWithText(imageText)

    # Save image to a bytes buffer
    img_io = BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimeType="image/jpeg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)