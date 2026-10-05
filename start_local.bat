@echo off
title Smart Reminder ML - Local Server
echo ====================================================
echo Starting Smart Reminder Machine Learning Web App...
echo ====================================================
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:5000"
python app.py
pause
