$ErrorActionPreference = "Stop"
$workingDir = "D:\Đồ_án_2 - Copy"
Set-Location $workingDir
xelatex -interaction=nonstopmode slide_do_an.tex
if ($LASTEXITCODE -eq 0) {
    Write-Host "Compilation successful!" -ForegroundColor Green
} else {
    Write-Host "Compilation failed. Check slide_do_an.log for errors." -ForegroundColor Red
    exit 1
}
