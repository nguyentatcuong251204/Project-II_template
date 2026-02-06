# Compile slide_do_an.tex to PDF
$ErrorActionPreference = "Continue"
$workingDir = Join-Path $PSScriptRoot "."
Set-Location $workingDir

Write-Host "Compiling slide_do_an.tex..." -ForegroundColor Yellow

# Run xelatex twice for proper references
xelatex -interaction=nonstopmode slide_do_an.tex
if ($LASTEXITCODE -ne 0) {
    Write-Host "First compilation failed. Check slide_do_an.log" -ForegroundColor Red
    exit 1
}

xelatex -interaction=nonstopmode slide_do_an.tex
if ($LASTEXITCODE -ne 0) {
    Write-Host "Second compilation failed. Check slide_do_an.log" -ForegroundColor Red
    exit 1
}

Write-Host "Compilation successful! PDF created: slide_do_an.pdf" -ForegroundColor Green
