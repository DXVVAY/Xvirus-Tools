@echo off

cd /d %~dp0

pip install -U -r requirements.txt
pip install cairocffi
pipwin install cairocffi
pip install cairosvg

echo @echo off > start.bat
echo python -m Xvirus >> start.bat
echo pause >> start.bat
echo exit >> start.bat
start start.bat

pause
exit