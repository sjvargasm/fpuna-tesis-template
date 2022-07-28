from pathlib import Path
from os import remove, system


# Elimina archivos con las extensiones en patterns (archivos de compilación auxilares)
def clean(fichero="./"):
    patterns = ("*-blx.bib", ".syntex.gz", "*.aux", "*.log", "*.blg", "*.bcf", "*.run.xml",
                "*.lof", "*.toc", "*.fdb_latexmk", "*.orig", "*.loa", "*.snm", "*.nav", "*.out", "*.bbl", "*.fls", "*.lot")
    for pattern in patterns:
        for path in Path(fichero).glob("**/" + pattern):
            remove(path)


# Ejecuta la secuencia de compilación pdflatex -> biber -> pdflatex x 2 sobre el archivo nombre.tex del fichero
def build(nombre, fichero="./", secuencia=True):
    if secuencia:
        secuence = [0, 1, 0, 0]
        command = ("pdflatex", "biber")
        for number in secuence:
            system("cd " + fichero + "; " + command[number] + " " + nombre)
    else:
        system("cd " + fichero + "; pdflatex " + nombre)


# Compila y limpia archivos auxiliares
def cleanbuild(nombre, folder="book", secuencia=True):
    clean(folder)
    build(nombre, folder, secuencia)
    clean(folder)
