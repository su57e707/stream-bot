# Start from a standard Microsoft base image for dev containers
FROM mcr.microsoft.com/devcontainers/python:3.10

# Switch to the root user to install system-level software
USER root

# Install Google Chrome, Xvfb (the virtual screen), and audio/video libraries
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    wget xvfb pulseaudio \
    # Dependencies for Chrome
    libxss1 libappindicator1 libindicator7 gconf-service libasound2 libnspr4 \
    libnss3 libxtst6 ca-certificates fonts-liberation libappindicator3-1 \
    libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcups2 libdbus-1-3 \
    libdrm2 libgbm1 libgconf-2-4 libgdk-pixbuf2.0-0 libgtk-3-0 \
    libu2f-udev libvulkan1 libx11-xcb1 libxcb-dri3-0 libxcomposite1 \
    libxdamage1 libxext6 libxfixes3 libxrandr2 libxshmfence1

# Download and install the official Google Chrome package
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Switch back to the default, non-root user for security
USER vscode
