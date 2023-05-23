@echo off

for /f "delims=" %%i in (requirements.txt) do (
    echo Installing %%i
    python -m pip install "%%i"
)

cls

echo python Xvirus.py >> start.bat

start start.bat
