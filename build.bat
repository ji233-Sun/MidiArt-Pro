@echo off
REM MidiArt-Pro Windows Build Script
REM This script builds the MidiArt-Pro executable for Windows

echo ========================================
echo MidiArt-Pro Windows Build Script
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or later
    pause
    exit /b 1
)

echo Python found, proceeding with build...

REM Install/upgrade pip
echo Installing/upgrading pip...
python -m pip install --upgrade pip

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
python -m pip install pyinstaller

REM Install project dependencies
echo Installing project dependencies...
python -m pip install -r requirements.txt

REM Run the build script
echo Running build script...
python build.py

if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)

echo Build completed successfully!
echo Check the 'dist-final' directory for the executable.
pause
