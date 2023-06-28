import PyInstaller.__main__

PyInstaller.__main__.run([
    'xvirus.py',
    '--onefile',
    '--add-data', 'util;util',
    '--icon', 'D:/xvirus-tools/assets/icons/xvirusicon.png'  # Replace 'path/to/icon' with the path to your image file
])
