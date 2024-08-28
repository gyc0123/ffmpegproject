@echo off
rem Passing Windows PATH to MSYS2

set "ORIGINAL_PATH=%PATH%"
set "NEW_PATH="
echo %ORIGINAL_PATH%
rem Convert Windows PATH to MSYS2 format
for %%I in (%ORIGINAL_PATH%) do (
    echo %%I
    set "NEW_PATH=!NEW_PATH!:%%~dpI"
)
echo %NEW_PATH%
rem Run MSYS2 bash with the modified PATH
C:\msys64\usr\bin\bash.exe -lc "export PATH=$NEW_PATH:$PATH; echo $PATH"

pause