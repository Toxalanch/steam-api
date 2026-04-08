@echo off
REM the location of the steamcmd install
set LOCATION=%1
REM the login credentials of the steam user
set USERNAME=%2
set PASSWORD=%3
REM the app id for the game
set APPID=%4
cd /d %LOCATION%

REM runs steamcmd.exe then runs each other command in it
REM +login logs in with USERNAME and PASSWORD, does not work if steam guard is enabled. Would recommend creating another account under a family account
REM +app_update makes sure that game is both installed and updated, and makes sure that if using a family account, the DRM information (I'm guessing thats why it won't run even if the game is installed otherwise) even if the game is installed
REM +app_run runs the game based on the appid
REM +exit exits the steamcmd cli when the process is finished
steamcmd.exe -arg1 +login %USERNAME% %PASSWORD% +app_update %APPID% +app_run %APPID% +exit