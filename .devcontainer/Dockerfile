# Start from the official Microsoft Python dev container image
FROM mcr.microsoft.com/devcontainers/python:3.10

# Switch to the root user to install system packages
USER root

# --- SIMPLIFIED & CORRECTED INSTALLATION ---
# Install only the essential dependencies for Chrome and Xvfb
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    wget \
    xvfb \
    # Minimal dependencies for Chrome to run headlessly
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxtst6 \
    xdg-utils

# Download and install the official Google Chrome package
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Clean up apt-get cache to save space
RUN rm -rf /var/lib/apt/lists/*

# Switch back to the default, non-root user for security
USER vscode
