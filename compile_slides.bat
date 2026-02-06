@echo off
chcp 65001 >nul
cd /d "%~dp0"
xelatex -interaction=nonstopmode slide_do_an.tex
xelatex -interaction=nonstopmode slide_do_an.tex
if errorlevel 1 (
    echo.
    echo Compilation failed. Please check slide_do_an.log for errors.
    pause
    exit /b 1
) else (
    echo.
    echo Compilation successful! PDF file: slide_do_an.pdf
    pause
)
