from pathlib import Path
from os import remove, system


# Elimina archivos con las extensiones en patterns (archivos de compilación auxilares)
def limpiar(fichero):
    patrones = ("*-blx.bib", ".syntex.gz", "*.aux", "*.log", "*.blg", "*.bcf", "*.run.xml",
                "*.lof", "*.toc", "*.fdb_latexmk", "*.orig", "*.loa", "*.snm", "*.nav", "*.out", "*.bbl", "*.fls", "*.lot")
    for patron in patrones:
        for archivo in Path(fichero).glob("**/" + patron):
            remove(archivo)


# Ejecuta la secuencia de compilación pdflatex -> biber -> pdflatex x 2 sobre el archivo nombre.tex del fichero
def compilar(nombre, fichero, conSecuencia=True):
    if conSecuencia:
        secuencia = [0, 1, 0, 0]
        command = ("pdflatex", "biber")
        for number in secuencia:
            system("cd " + fichero + "; " + command[number] + " " + nombre)
    else:
        system("cd " + fichero + "; pdflatex " + nombre)


# Compila y limpia archivos auxiliares
def limpiar_compilar(nombre, fichero="book", secuencia=True):
    limpiar(fichero)
    compilar(nombre, fichero, secuencia)
    limpiar(fichero)
