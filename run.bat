@echo off
setlocal

REM Define Python executable and paths
set PYTHON=python
set VENV_DIR=venv
set SCRIPT=script.py

REM Create virtual environment if it doesn't exist
if not exist %VENV_DIR% (
    %PYTHON% -m venv %VENV_DIR%
)

REM Activate virtual environment
call %VENV_DIR%\Scripts\activate

REM Upgrade pip and install dependencies
pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
)

REM Run the Python script
%PYTHON% %SCRIPT%

REM Deactivate virtual environment
deactivate

endlocal