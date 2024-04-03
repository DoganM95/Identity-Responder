# Stop and remove any running image response cotainer
docker ps -a | Select-String "image" | ForEach-Object { docker rm -f $_.ToString().Split(" ")[0] }

# Remove dangling images
docker image prune -f

# Build the image
docker build -t ip-image-server .

# Run a container
docker run -p 4000:8080 ip-image-server