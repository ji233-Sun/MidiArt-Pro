# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect data files for various packages
datas = []

# Add font files
datas += [('SourceHanSansSC-Bold.otf', '.')]
datas += [('SourceHanSansSC-Regular.otf', '.')]

# Add presets directory
datas += [('presets', 'presets')]

# Add images directory if it exists
if os.path.exists('images'):
    datas += [('images', 'images')]

# Collect data files for packages that need them
try:
    datas += collect_data_files('customtkinter')
except:
    pass

try:
    datas += collect_data_files('librosa')
except:
    pass

try:
    datas += collect_data_files('pygame')
except:
    pass

# Hidden imports for packages that might not be detected automatically
hiddenimports = [
    'customtkinter',
    'mido',
    'moviepy.editor',
    'librosa',
    'pygame',
    'cv2',
    'numpy',
    'tkinter',
    'tkinter.filedialog',
    'threading',
    'collections',
    'json',
    'math',
    'random',
    'time',
    'sys',
    'os',
    # Additional hidden imports for moviepy
    'moviepy.video.io.VideoFileClip',
    'moviepy.audio.io.AudioFileClip',
    # Additional hidden imports for librosa
    'librosa.core',
    'librosa.feature',
    'librosa.util',
    # Additional hidden imports for pygame
    'pygame.mixer',
    'pygame.display',
    'pygame.draw',
    'pygame.font',
    'pygame.image',
    'pygame.surface',
    # Additional hidden imports for customtkinter
    'customtkinter.windows',
    'customtkinter.widgets',
]

# Collect all submodules for critical packages
try:
    hiddenimports += collect_submodules('customtkinter')
except:
    pass

try:
    hiddenimports += collect_submodules('librosa')
except:
    pass

a = Analysis(
    ['visualizer.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MidiArt-Pro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False for GUI application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MidiArt-Pro',
)

# For macOS, create an app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name='MidiArt-Pro.app',
        icon='icon.ico' if os.path.exists('icon.ico') else None,
        bundle_identifier='com.aclameta.midiart-pro',
        info_plist={
            'CFBundleName': 'MidiArt Pro',
            'CFBundleDisplayName': 'MidiArt Pro',
            'CFBundleVersion': '1.0.0',
            'CFBundleShortVersionString': '1.0.0',
            'NSHighResolutionCapable': True,
        },
    )
