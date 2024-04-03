# Intro
A server that responds to clients with a picture, showing their identity like IP, Geo-Location, ISP, Country, Userclient, etc. 

## Setup 

- Get a linux machine ready to serve the container
- Start the container using  
  ```shell
  docker run \
    -d \
    -e "IPINFO_ACCESS_TOKEN=tokenGoesHere" \
    -p 4000:4000 \
    ghcr.io/doganm95/identity-responder
  ```
- Forward the port of the machine it runs on to the internet, here port `4000`

## Usage

- Open the page using any browser (`GET` request) to the page, e.g.  `myhome.ddns.com:4000`
- Receive a jpeg containing the client's info

## Notes

The machine this container this container runs on should be exposed to the web via port forwarding.   
Only then, the external ip / domain-name where the container runs can be called to show the real external ip.  
If a `GET` request is made inside the same LAN, it will just show the client's internal IP.  
