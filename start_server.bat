
@echo off

set PYTHON_SCRIPT_NAME=api
set PORT=8000

call .venv\Scripts\activate.bat
python -m ensurepip --upgrade
pip install -r requirements.txt
echo Requirements.txt installed
timeout /t 1
cls

color 0C
echo Server startup started!
for /f "tokens=14" %%i in ('ipconfig ^| findstr /i "ipv4"') do set LOCAL_IP=%%i
echo Server address: %LOCAL_IP%:%PORT%
echo Local address: https://127.0.0.1:%PORT%
echo Python script name: %PYTHON_SCRIPT_NAME%
timeout /t 1
python -m uvicorn %PYTHON_SCRIPT_NAME%:app --port %PORT% --reload --ssl-keyfile=secrets/key.pem --ssl-certfile=secrets/cert.pem
pause