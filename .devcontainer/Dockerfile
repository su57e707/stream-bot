# Start from the official Microsoft Python dev container image
FROM mcr.microsoft.com/devcontainers/python:3.10

# Switch to the root user to install system packages
USER root

# --- AGGRESSIVE & CORRECTED INSTALLATION ---
# Force apt-get to update its package lists before trying to install.
RUN apt-get update

# Install xvfb separately and first to ensure it is present.
RUN apt-get install -y xvfb

# Now, install Google Chrome and its other dependencies.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Clean up the package cache to save space
RUN rm -rf /var/lib/apt/lists/*

# Switch back to the default, non-root user for security
USER vscode
