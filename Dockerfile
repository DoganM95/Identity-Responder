FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy source file
COPY ./app.py app.py

# Install dependencies
RUN pip install --no-cache-dir Flask Pillow
RUN pip install --upgrade Pillow

# Expose the app port
EXPOSE 8080

# Execute the app
CMD ["python", "app.py"]