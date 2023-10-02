@echo off
setlocal enabledelayedexpansion

set "scriptPath=C:\PATH\TO\discordgm.py"
set "logFile=C:\PATH\TO\log.txt"

:: Get the current date in the format YYYYMMDD
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (
    set "currentDate=%%c%%b%%a"
)

:: Check if the log file exists
if not exist "%logFile%" (
    echo %currentDate% > "%logFile%"
)

:: Read the last run date from the log file
set /p lastRunDate=<"%logFile%"

:: Compare the current date with the last run date
if %currentDate% neq %lastRunDate% (
    echo Running the script...
    python %scriptPath%
    echo %currentDate%
    echo %lastRunDate%
    :: Update the last run date in the log file
    echo %currentDate% > "%logFile%"
) else (
    echo Script already run today. Exiting...
)
endlocal
