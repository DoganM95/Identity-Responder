from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

def createImageWithText(text, imageSize=(300, 200), fontSize=20):
    image = Image.new('RGB', imageSize, color='black')  # RGB image with 300x200 and background color black
    draw = ImageDraw.Draw(image)  # Create the drawable image
    try:
        font = ImageFont.truetype("arial.ttf", fontSize)  # Attempt to set font details
    except IOError:
        font = ImageFont.load_default()
        print("Default font loaded.")
    textWidth, textHeight = draw.textsize(text, font=font)  # Measure text size
    position = ((imageSize[0] - textWidth) / 2, (imageSize[1] - textHeight) / 2)  # Center text
    draw.text(position, text, fill="white", font=font)  # Add white text on black background
    return image

@app.route("/")
def home():
    userIp = request.remote_addr  # Correct variable name to match the format string
    imageText = f"Your IP: {userIp}"  # Use formatted string literal to include user IP
    image = createImageWithText(imageText)

    # Save image to a bytes buffer
    img_io = BytesIO()
    image.save(img_io, 'JPEG', quality=70)  # Specify JPEG quality (optional)
    img_io.seek(0)

    return send_file(img_io, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
