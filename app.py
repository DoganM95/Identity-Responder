from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

def createImageWithText(text, imageSize=(300, 200), fontSize=20):
    # Create a blank image
    image = Image.new('RGB', imageSize, color='black')
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Attempt to use a specific font
    try:
        font = ImageFont.truetype("arial.ttf", fontSize)
    except IOError:
        # If specific font is not found, use the default font
        font = ImageFont.load_default()
        print("Default font loaded.")
    
    # Calculate position to center the text
    position = ((imageSize[0]) / 2, (imageSize[1]) / 2)
    
    # Draw the text on the image
    draw.text(position, text, fill="white", font=font)
    
    return image

@app.route("/")
def home():
    # Get the user's IP address
    userIp = request.remote_addr
    imageText = f"Your IP: {userIp}"
    
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
    app.run(host='0.0.0.0', port=8080)
