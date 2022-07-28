from pathlib import Path
from os import remove, system
from platform import system as psystem

if psystem().startswith("win"):
    cd = "dir "
else:
    cd = "cd "


def clean(folder="./"):
    patterns = ("*-blx.bib", ".syntex.gz", "*.aux", "*.log", "*.blg", "*.bcf", "*.run.xml",
                "*.lof", "*.toc", "*.fdb_latexmk", "*.orig", "*.loa", "*.snm", "*.nav", "*.out", "*.bbl", "*.fls", "*.lot")
    for pattern in patterns:
        for path in Path(folder).glob("**/" + pattern):
            remove(path)


def build(name, folder="./"):
    secuence = [0, 1, 0, 0, 2]
    command = ("pdflatex", "biber", "evince")
    for number in secuence:
        system(cd + folder + "; " +
               command[number] + " " + name + (".pdf" if number == 2 else " "))


def build_ppt(name, folder="./"):
    system(cd + folder + "; pdflatex " + name)
    system(cd + folder + "; evince " + name + ".pdf")
