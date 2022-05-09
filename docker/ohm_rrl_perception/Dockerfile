# Dockerfile for generating a docker image running
# ROS kinetic with find 2d object package for hazmat detection

FROM ros:kinetic-perception-xenial

MAINTAINER bausma

# Update & Upgrade
RUN apt-get -y update \
    && apt-get -y upgrade

# Install tools
RUN apt-get -y install \
    ros-kinetic-find-object-2d \
    qt4-default \
    libzbar-dev

# Create location for repository
RUN mkdir /opt/ros/kinetic/src

# Change work directory to ros
WORKDIR /opt/ros/kinetic/src

# Clone git repo for hazmat detection
RUN git clone https://github.com/autonohm/ohm_rrl_perception.git

# Change workdir to folder
WORKDIR /opt/ros/kinetic/src/ohm_rrl_perception

# Checkout branch
RUN git checkout d79e9b7bf56d14d0926423a3f62f66731f016f9c

# Remove unused folders
RUN rm -r ohm_rrl_cdetection 

# Change workdir to ROS
WORKDIR /opt/ros/kinetic

# Set rosmaster
ENV ROS_MASTER=localhost
ENV ROS_MASTER_URI=http://localhost:11311/
ENV ROS_HOSTNAME=localhost
ENV ROS_IP=localhost

# Build hazmat node
RUN /bin/bash -c 'source setup.bash && catkin_make'

# Copy edited launchfile
COPY ohm_rrl_perception/hazmat.launch /opt/ros/kinetic/src/ohm_rrl_perception/ohm_rrl_perception_launch/launch

# Launch node
CMD /bin/bash -c "source devel/setup.bash && roslaunch ohm_rrl_perception_launch hazmat.launch"
