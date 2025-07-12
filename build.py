#!/usr/bin/env python3
"""
MidiArt-Pro Build Script
Automated build script for creating distributable executables using PyInstaller.
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

def run_command(command, description=""):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"Running: {description or command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=False, text=True)
        print(f"✅ Success: {description or command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description or command}")
        print(f"Exit code: {e.returncode}")
        return False

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'pyinstaller',
        'customtkinter',
        'mido',
        'moviepy',
        'librosa',
        'pygame',
        'opencv-python',
        'numpy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        install_cmd = f"{sys.executable} -m pip install {' '.join(missing_packages)}"
        if not run_command(install_cmd, "Installing missing packages"):
            return False
    
    return True

def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous build artifacts...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['*.pyc', '*.pyo']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Removed directory: {dir_name}")
    
    # Clean .pyc files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.pyc', '.pyo')):
                os.remove(os.path.join(root, file))

def build_executable():
    """Build the executable using PyInstaller."""
    print("🔨 Building executable with PyInstaller...")
    
    # Check if spec file exists
    spec_file = "MidiArt-Pro.spec"
    if not os.path.exists(spec_file):
        print(f"❌ Spec file {spec_file} not found!")
        return False
    
    # Run PyInstaller
    build_cmd = f"pyinstaller {spec_file}"
    if not run_command(build_cmd, "Building with PyInstaller"):
        return False
    
    return True

def create_distribution():
    """Create distribution package."""
    print("📦 Creating distribution package...")
    
    system = platform.system()
    dist_dir = Path("dist")
    
    if not dist_dir.exists():
        print("❌ Build directory not found!")
        return False
    
    # Create final distribution directory
    final_dist = Path("dist-final")
    final_dist.mkdir(exist_ok=True)
    
    if system == "Windows":
        # Create ZIP for Windows
        app_dir = dist_dir / "MidiArt-Pro"
        if app_dir.exists():
            zip_name = final_dist / "MidiArt-Pro-Windows.zip"
            shutil.make_archive(str(zip_name.with_suffix('')), 'zip', str(app_dir))
            print(f"✅ Created: {zip_name}")
        else:
            print("❌ Windows build directory not found!")
            return False
            
    elif system == "Darwin":  # macOS
        # Create ZIP for macOS
        app_bundle = dist_dir / "MidiArt-Pro.app"
        if app_bundle.exists():
            zip_name = final_dist / "MidiArt-Pro-macOS.zip"
            shutil.make_archive(str(zip_name.with_suffix('')), 'zip', str(dist_dir), "MidiArt-Pro.app")
            print(f"✅ Created: {zip_name}")
        else:
            print("❌ macOS app bundle not found!")
            return False
            
    else:  # Linux
        # Create ZIP for Linux
        app_dir = dist_dir / "MidiArt-Pro"
        if app_dir.exists():
            zip_name = final_dist / "MidiArt-Pro-Linux.zip"
            shutil.make_archive(str(zip_name.with_suffix('')), 'zip', str(app_dir))
            print(f"✅ Created: {zip_name}")
        else:
            print("❌ Linux build directory not found!")
            return False
    
    return True

def main():
    """Main build process."""
    print("🚀 MidiArt-Pro Build Script")
    print(f"Platform: {platform.system()} {platform.machine()}")
    print(f"Python: {sys.version}")
    
    # Step 1: Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed!")
        sys.exit(1)
    
    # Step 2: Clean previous builds
    clean_build()
    
    # Step 3: Build executable
    if not build_executable():
        print("❌ Build failed!")
        sys.exit(1)
    
    # Step 4: Create distribution
    if not create_distribution():
        print("❌ Distribution creation failed!")
        sys.exit(1)
    
    print("\n🎉 Build completed successfully!")
    print("📁 Check the 'dist-final' directory for the distribution package.")

if __name__ == "__main__":
    main()
