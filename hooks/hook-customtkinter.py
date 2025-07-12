# PyInstaller hook for customtkinter
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all data files from customtkinter
datas = collect_data_files('customtkinter')

# Collect all submodules
hiddenimports = collect_submodules('customtkinter')

# Add specific modules that might be missed
hiddenimports += [
    'customtkinter.windows',
    'customtkinter.widgets',
    'customtkinter.appearance_mode',
    'customtkinter.theme_manager',
    'customtkinter.settings',
    'customtkinter.utility',
]
