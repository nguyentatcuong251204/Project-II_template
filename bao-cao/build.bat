@echo off
setlocal EnableDelayedExpansion
:: =======================================================
::  Build script cho bao-cao-mau.tex
::  Su dung XeLaTeX + Biber (ho tro tieng Viet Unicode)
::  Chay: double-click hoac goi tu terminal
:: =======================================================

SET TEXFILE=main
SET ENGINE=xelatex
for /f "usebackq delims=" %%P in (`powershell -NoProfile -Command "($env:Path -split ';' | Where-Object { $_ -and ($_ -notmatch '\.exe$') }) -join ';'"`) do set "PATH=%%P"

echo =============================================
echo  BUILD: %TEXFILE%.tex  [engine: %ENGINE%]
echo =============================================

echo.
echo [1/4] %ENGINE% pass 1...
%ENGINE% -interaction=nonstopmode %TEXFILE%.tex

echo.
echo [2/4] Biber (bibliography)...
biber %TEXFILE%

echo.
echo [3/4] %ENGINE% pass 2...
%ENGINE% -interaction=nonstopmode %TEXFILE%.tex

echo.
echo [4/4] %ENGINE% pass 3 (cross-references)...
%ENGINE% -interaction=nonstopmode %TEXFILE%.tex

echo.
echo =============================================
echo  BUILD DA HOAN TAT (Bo qua cac canh bao de build bang duoc)!
echo  Kiem tra %TEXFILE%.pdf de xem ket qua.
echo =============================================
start %TEXFILE%.pdf
goto end

:error
echo.
echo [LOI] Build that bai nghiem trong! Xem %TEXFILE%.log de biet them.
echo.
pause

:end
