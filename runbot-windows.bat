@echo off
echo.
echo Starting codex.py...
echo.
:loop
    venv\scripts\python.exe codex.py
    echo.
    echo Restarting codex.py...
    echo.
    timeout 5 > nul
goto loop