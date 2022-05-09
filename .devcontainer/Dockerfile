ARG VARIANT="galactic"
FROM franc0r/ros2-francor-dev:${VARIANT}

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    |  sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu focal stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && sudo apt-get update \
    && sudo apt-get install -y \
    docker-ce docker-ce-cli docker-compose
    
USER root

RUN mkdir -p /root/ros2_ws/src \
    && echo "source /opt/ros/galactic/setup.bash" >> /root/.bashrc
