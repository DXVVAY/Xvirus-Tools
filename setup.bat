@echo off
setlocal

echo Installing curl...
choco install curl -y

echo Downloading Python installer...
curl -L -o python-installer.exe https://www.python.org/ftp/python/latest/python-3.10.0-amd64.exe

echo Installing Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

echo Cleaning up...
del python-installer.exe

echo Installing Python packages...
pip install -U -r requirements.txt
pipwin install cairocffi

echo Starting Python script...
echo @echo off > start.bat
echo python -m Xvirus >> start.bat
echo pause >> start.bat
echo exit >> start.bat
start start.bat

echo Done.
