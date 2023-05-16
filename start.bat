@echo off

REM clear the console
cls

:begin

REM print option menu
echo STTS script made by Lupiax
echo.
echo [1] Launch English STTS
echo [2] Launch Japanese STTS
echo [3] Install Voicevox Engine (docker)
echo [4] Start Voicevox Engine (docker)
echo [5] Get Audio Devices
echo [6] Exit
echo.

REM make the user select one option.
set choice=
set /p choice=Choose: 

REM process selection
if not '%choice%'=='' set choice=%choice:~0,1%

if '%choice%'=='1' goto start_en
if '%choice%'=='2' goto start_jp
if '%choice%'=='3' goto install_voicevox
if '%choice%'=='4' goto start_voicevox
if '%choice%'=='5' goto get_devices
if '%choice%'=='6' goto script_exit

ECHO "%choice%" is not a valid choice, try again.

goto begin

:start_en

REM clear the console
cls

REM start the python script
python scripts/stts-en.py

:start_jp

REM clear the console
cls

REM start the python script
python scripts/stts-jp.py

:install_voicevox

call utils/install_voicevox.bat

REM clear the console
cls

goto begin

:start_voicevox

call utils\start_voicevox.bat

REM clear the console
cls

echo Started voicevox engine.

goto begin

:get_devices

REM clear the console
cls

python scripts/get_devices.py

pause

REM clear the console
cls

goto begin

:script_exit

REM clear the console
cls

ECHO exiting...

REM kill the program.
pause