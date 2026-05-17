import os

files = [
    r"d:\BS_thesis\DATN\Report\chapter_datn\theory.tex",
    r"d:\BS_thesis\DATN\Report\chapter_datn\methodology.tex",
    r"d:\BS_thesis\DATN\Report\chapter_datn\research_gap.tex"
]

replacements = {
    r"\mathcal{Z}": r"\mathbf{Z}",
    r"\mathcal{G}": r"\mathbf{G}",
    r"\mathcal{L}": r"\mathbf{L}",
    r"\mathcal{T}": r"\mathbf{T}",
    r"\mathcal{K}": r"\mathbf{K}",
    r"\mathcal{X}": r"\mathbf{X}",
    r"\mathcal{D}": r"\mathbf{D}",
    r"\mathcal{S}": r"\mathbf{S}",
    r"\mathcal{A}": r"\mathbf{A}",
    r"\mathcal{GP}": r"\mathrm{GP}",
    r"\mathcal{H}": r"H",
    r"\mathcal{P}": r"\mathbf{P}",
    r"\mathcal{J}": r"J"
}

for fp in files:
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fp}")
