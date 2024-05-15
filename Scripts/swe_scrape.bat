@echo off
rem Get the current letter of the drive the batch file is located in
cd /d %~d0
echo Current Drive: %~d0

rem Set Python path
set PYTHONPATH=%PYTHONPATH%;D:\SweScrapper

rem Define the Python script path
set "scrape_swe=%~d0\SweScrapper\Scripts\gui.py"

rem Activate the virtual environment
call %~d0\SweScrapper\venv\Scripts\activate.bat

rem Run the Python script
python "%scrape_swe%"

pause