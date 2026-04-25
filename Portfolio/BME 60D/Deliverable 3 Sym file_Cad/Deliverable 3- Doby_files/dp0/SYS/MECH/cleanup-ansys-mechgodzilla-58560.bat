@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="mechgodzilla" (taskkill /f /pid 44180)
if /i "%LOCALHOST%"=="mechgodzilla" (taskkill /f /pid 65916)
if /i "%LOCALHOST%"=="mechgodzilla" (taskkill /f /pid 3440)
if /i "%LOCALHOST%"=="mechgodzilla" (taskkill /f /pid 58560)

del /F cleanup-ansys-mechgodzilla-58560.bat
