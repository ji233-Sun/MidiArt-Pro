#!/bin/bash
# MidiArt-Pro Unix Build Script
# This script builds the MidiArt-Pro executable for Linux/macOS

set -e  # Exit on any error

echo "========================================"
echo "MidiArt-Pro Unix Build Script"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or later"
    exit 1
fi

echo "Python found: $(python3 --version)"

# Check if we're on macOS and install system dependencies
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS, checking for Homebrew dependencies..."
    if command -v brew &> /dev/null; then
        echo "Installing/updating system dependencies with Homebrew..."
        brew install portaudio || true
        brew install ffmpeg || true
    else
        echo "Warning: Homebrew not found. Some dependencies might be missing."
        echo "Please install Homebrew and run: brew install portaudio ffmpeg"
    fi
fi

# Check if we're on Linux and install system dependencies
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux, checking for system dependencies..."
    if command -v apt-get &> /dev/null; then
        echo "Installing system dependencies with apt..."
        sudo apt-get update
        sudo apt-get install -y \
            libgl1-mesa-dev \
            libglib2.0-0 \
            libsm6 \
            libxext6 \
            libxrender-dev \
            libgomp1 \
            libfontconfig1 \
            libice6 \
            libxrandr2 \
            libxss1 \
            libxtst6 \
            libxi6 \
            libxcomposite1 \
            libxdamage1 \
            libxfixes3 \
            libxcursor1 \
            libasound2-dev \
            portaudio19-dev \
            ffmpeg
    elif command -v yum &> /dev/null; then
        echo "Installing system dependencies with yum..."
        sudo yum install -y \
            mesa-libGL \
            glib2 \
            libSM \
            libXext \
            libXrender \
            libgomp \
            fontconfig \
            libICE \
            libXrandr \
            libXScrnSaver \
            libXtst \
            libXi \
            libXcomposite \
            libXdamage \
            libXfixes \
            libXcursor \
            alsa-lib-devel \
            portaudio-devel \
            ffmpeg
    else
        echo "Warning: Package manager not detected. Please install system dependencies manually."
    fi
fi

# Install/upgrade pip
echo "Installing/upgrading pip..."
python3 -m pip install --upgrade pip

# Install PyInstaller if not already installed
echo "Installing PyInstaller..."
python3 -m pip install pyinstaller

# Install project dependencies
echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt

# Make the build script executable
chmod +x build.py

# Run the build script
echo "Running build script..."
python3 build.py

echo "Build completed successfully!"
echo "Check the 'dist-final' directory for the executable."
