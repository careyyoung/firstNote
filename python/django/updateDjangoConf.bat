@echo off
rem var1 backup folder
rem var2 backuped folder
rem var3 update folder

set var1=C:\app\Python27\Lib\site-packages\django\conf
set var2=C:\app\Python27\Lib\site-packages\django\conf_backup
set var3=E:\eclipse_git\firstNote\python\django\django-conf

echo.
echo.
echo ### backup folder ###
move %var1% %var2%
IF ERRORLEVEL 1 goto failed1
IF ERRORLEVEL 0 ECHO backup success!!!

echo.
echo.
echo ### xcopy folder ###
xcopy /e /i /q %var3% %var1%
IF ERRORLEVEL 1 goto failed2
IF ERRORLEVEL 0 ECHO xcopy success!!!

echo.
echo.
echo ### delete backup ###
rd /s /q %var2%
IF ERRORLEVEL 1 goto failed3
IF ERRORLEVEL 0 goto success

:failed1
ECHO backup failed
goto exit

:failed2
ECHO copy failed
goto exit

:failed3
ECHO delete failed
goto exit

:success
ECHO success!!!  
ECHO all done!!!
goto exit

:exit
echo.
pause
