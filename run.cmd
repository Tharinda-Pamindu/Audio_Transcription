@echo off
title Audio Transcription — Whisper AI
color 0B

echo.
echo  ╔══════════════════════════════════════════════════╗
echo  ║   Audio Transcription — Whisper + Liquid Glass   ║
echo  ╚══════════════════════════════════════════════════╝
echo.

REM --- Check Python ---
where python >nul 2>nul
if errorlevel 1 (
    echo  [ERROR] Python is not installed or not in PATH.
    echo          Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM --- Check FFmpeg ---
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo  [WARNING] FFmpeg not found in PATH.
    echo            Whisper requires FFmpeg for audio decoding.
    echo            Install from: https://ffmpeg.org/download.html
    echo.
    echo  Press any key to continue anyway, or Ctrl+C to cancel...
    pause >nul
)

REM --- Change to script directory ---
cd /d "%~dp0"

REM --- Create venv if needed ---
if not exist ".venv\Scripts\activate.bat" (
    echo  [1/3] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo  [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo        Done.
) else (
    echo  [1/3] Virtual environment found.
)

REM --- Activate venv ---
call .venv\Scripts\activate.bat

REM --- Install / update dependencies ---
echo  [2/3] Installing dependencies (first run may take a while)...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo  [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)
echo        Done.

REM --- Launch app ---
echo  [3/3] Starting server...
echo.
echo  ┌──────────────────────────────────────────────────┐
echo  │  Open your browser at:                           │
echo  │  http://127.0.0.1:5000                           │
echo  │                                                  │
echo  │  Press Ctrl+C to stop the server.                │
echo  └──────────────────────────────────────────────────┘
echo.

REM --- Open browser after a short delay ---
start "" "http://127.0.0.1:5000"

REM --- Run Flask ---
python app.py

pause
