# Installation

Official Install Script:
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
sudo systemctl status docker
```

# Pull Images
```bash
docker pull nginx    # Pull Latest Images
docker images        # List Images
```

# Run Images
`-d` -> Background Run
`-p` -> Port Mapping
    [para] Ext: Int
`--name` -> docker ps name
`-v` -> File Mapping
```bash
docker run -d -p 80:80 nginx
docker run -d -p 8080:80 -v `pwd`:/usr/share/nginx/html nginx
docker ps                                  # List Processes
docker exec -it <id> bash                  # Get Into a container
docker rm -f <id>                          # Delete Container
```

# Commit Containers
```bash
docker commit <id> <Images Name>
```

# Build from docker file
```bash
docker build -t <Images Name> .
```

# Save Images to .tar
```bash
docker save <Images Name> > <fileName>.tar
```

# Load .tar to Images
```bash
docker load < <fileName>.tar
```
