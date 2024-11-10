#!/bin/bash

# Exit on any error
set -e

# Create necessary directories
sudo mkdir -p /opt/llama_api
sudo mkdir -p /opt/llama_models

# Set permissions
sudo chown -R $USER:$USER /opt/llama_api
sudo chown -R $USER:$USER /opt/llama_models

# Install system dependencies
sudo apt update
sudo apt install -y python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv /opt/llama_api/venv
source /opt/llama_api/venv/bin/activate

# Install Python dependencies
pip install -r /workspace/opt/llama_api/requirements.txt

# Install systemd service
sudo cp /workspace/opt/llama_api/systemd/llama-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable llama-api
sudo systemctl start llama-api

echo "Installation completed successfully!"
echo "Check service status with: sudo systemctl status llama-api"
