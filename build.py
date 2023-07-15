import os
import subprocess

import PyInstaller.__main__

os.makedirs('dist/util', exist_ok=True)

subprocess.run(['pyarmor', 'obfuscate', 'Xvirus.py'])

subprocess.run(['pyarmor', 'obfuscate', '--recursive', '-O', 'dist/util', 'util'])

PyInstaller.__main__.run([
    'Xvirus.py',
    '--onefile',
    '--add-data', 'dist/util;util',
    '--icon', 'D:/xvirus/xvirus/assets/icons/xicon.png',
    '--name', 'Xvirus-Tools',
    '--key', 'XvirusOnTopAndBBD',
    '--clean',
    '--upx-dir', 'path/to/upx',
    '--distpath', 'dist',
    '--workpath', 'build',
    '--noconfirm'
])
