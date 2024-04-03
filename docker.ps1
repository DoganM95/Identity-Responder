# Build the image
docker build -t ip-image-server .

# Run a container
docker run -p 4000:8080 ip-image-server