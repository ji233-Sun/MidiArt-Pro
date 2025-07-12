# MidiArt-Pro

A powerful and customizable MIDI music visualizer that turns your music into art. (一个强大且可定制的MIDI音乐可视化工具，将你的音乐变成艺术。)

![Build Status](https://github.com/YOUR_USERNAME/MidiArt-Pro/workflows/Build%20and%20Release%20MidiArt-Pro/badge.svg)
![License](https://img.shields.io/github/license/YOUR_USERNAME/MidiArt-Pro)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)

## ✨ Features

- 🎵 **MIDI Visualization**: Transform MIDI files into stunning visual art
- 🎨 **Customizable Themes**: Multiple color themes and visual styles
- 🎹 **Piano Tiles Mode**: Classic piano tiles visualization
- 🌊 **Soundscape Mode**: Experimental audio-reactive visualizations
- 📹 **Video Export**: Export your visualizations as high-quality MP4 videos
- 🎛️ **Advanced Controls**: Fine-tune vibration, fade effects, and timing
- 🌍 **Multi-language**: Support for Chinese, English, and Traditional Chinese
- 💾 **Preset System**: Save and load your favorite visualization settings

## 📥 Download

### Pre-built Releases
Download the latest release for your platform:

- **Windows**: [MidiArt-Pro-Windows.zip](https://github.com/YOUR_USERNAME/MidiArt-Pro/releases/latest)
- **macOS**: [MidiArt-Pro-macOS.zip](https://github.com/YOUR_USERNAME/MidiArt-Pro/releases/latest)
- **Linux**: [MidiArt-Pro-Linux.zip](https://github.com/YOUR_USERNAME/MidiArt-Pro/releases/latest)

### Installation
1. Download the appropriate file for your operating system
2. Extract the archive to your desired location
3. Run the executable file:
   - **Windows**: `MidiArt-Pro.exe`
   - **macOS**: Double-click `MidiArt-Pro.app`
   - **Linux**: `./MidiArt-Pro`

## 🛠️ Building from Source

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Quick Build
Use the provided build scripts for your platform:

#### Windows
```batch
# Run the batch script
build.bat
```

#### macOS/Linux
```bash
# Make the script executable and run it
chmod +x build.sh
./build.sh
```

#### Manual Build
```bash
# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Build the executable
pyinstaller MidiArt-Pro.spec

# The executable will be in the dist/ directory
```

### Build Requirements

#### System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get install -y \
    libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 \
    libxrender-dev libgomp1 libfontconfig1 libice6 \
    libxrandr2 libxss1 libxtst6 libxi6 libxcomposite1 \
    libxdamage1 libxfixes3 libxcursor1 libasound2-dev \
    portaudio19-dev ffmpeg
```

**macOS:**
```bash
brew install portaudio ffmpeg
```

**Windows:**
No additional system dependencies required.

## 🚀 Automated Deployment

This project includes a complete GitHub Actions workflow for automated building and releasing across multiple platforms.

### Setting up Automated Releases

1. **Fork or clone this repository**
2. **Update the repository URLs** in README.md and workflow files
3. **Create a release tag**:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
4. **The GitHub Action will automatically**:
   - Build executables for Windows, macOS, and Linux
   - Create a new release
   - Upload the built executables as release assets

### Manual Workflow Trigger
You can also trigger the build manually:
1. Go to the "Actions" tab in your GitHub repository
2. Select "Build and Release MidiArt-Pro"
3. Click "Run workflow"
4. Enter a version tag (e.g., v1.0.1)

## 📁 Project Structure

```
MidiArt-Pro/
├── visualizer.py           # Main application file
├── requirements.txt        # Python dependencies
├── MidiArt-Pro.spec       # PyInstaller configuration
├── build.py               # Cross-platform build script
├── build.bat              # Windows build script
├── build.sh               # Unix build script
├── version_info.py        # Version information for Windows
├── hooks/                 # PyInstaller hooks
│   └── hook-customtkinter.py
├── presets/               # Visualization presets
├── images/                # Application screenshots
├── .github/workflows/     # GitHub Actions workflows
│   └── build-and-release.yml
├── SourceHanSansSC-*.otf  # Font files
└── icon.ico               # Application icon
```

## 🎮 Usage

1. **Launch the application**
2. **Select your files**:
   - Click "选择 MIDI" to choose a MIDI file
   - Click "选择音频" to choose an audio file (MP3/WAV)
3. **Customize settings**:
   - Adjust resolution, BPM, and visual parameters
   - Choose color themes and visualization modes
   - Fine-tune effects and timing
4. **Start rendering**:
   - Click the render button to begin processing
   - Wait for the video to be generated
   - Find your output video in the project directory

## 🎨 Visualization Modes

- **Standard Mode**: Classic note visualization with customizable effects
- **Piano Tiles Mode**: Falling tiles visualization similar to popular mobile games
- **Solo Mode**: Focus on individual notes with enhanced effects
- **Soundscape Mode**: Experimental audio-reactive visualizations

## ⚙️ Configuration

### Presets
Save and load your favorite settings using the preset system:
- Use the preset dropdown to load existing configurations
- Modify settings and click "保存" to save new presets
- Presets are stored in the `presets/` directory as JSON files

### Advanced Settings
- **Vibration Effects**: Control note vibration intensity and timing
- **Fade Effects**: Adjust fade-in and fade-out durations
- **Compression**: Control vertical spacing of notes
- **Dynamic Range**: Choose between static and dynamic note range modes

## 🔧 Development

### Dependencies
The project uses the following main libraries:
- `customtkinter` - Modern GUI framework
- `mido` - MIDI file processing
- `moviepy` - Video processing and export
- `librosa` - Audio analysis
- `pygame` - Graphics rendering
- `opencv-python` - Video encoding
- `numpy` - Numerical computations

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Aclameta** - Original developer
- **AI Partner** - Development assistance
- **Open Source Community** - For the amazing libraries used in this project

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/MidiArt-Pro/issues) page
2. Create a new issue with detailed information
3. Include your operating system and error messages

## 🔄 Changelog

### v1.0.0
- Initial release
- Multi-platform support
- Automated build and release system
- Complete GUI with multiple visualization modes
- Preset system for saving configurations

---

**Made with ❤️ by Aclameta & AI Partner**
