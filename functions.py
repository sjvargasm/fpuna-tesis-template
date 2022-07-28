from pathlib import Path
from os import remove, system


# Elimina archivos con las extensiones en patterns (archivos de compilación auxilares)
def limpiar():
    patrones = ("*-blx.bib", ".syntex.gz", "*.aux", "*.log", "*.blg", "*.bcf", "*.run.xml",
                "*.lof", "*.toc", "*.fdb_latexmk", "*.orig", "*.loa", "*.snm", "*.nav", "*.out", "*.bbl", "*.fls", "*.lot")
    for patron in patrones:
        for direccion in Path("./").glob("**/" + patron):
            remove(direccion)  # TODO: Warn si archivo no existe


# Ejecuta la secuencia de compilación pdflatex -> biber -> pdflatex x 2 sobre el archivo nombre.tex del fichero
def compilar(nombre, fichero, conSecuencia):
    if conSecuencia:
        for number in [0, 1, 0, 0]:
            system("cd " + fichero + "; " +
                   ("pdflatex", "biber")[number] + " " + nombre)
    else:
        system("cd " + fichero + "; pdflatex " + nombre)


# Compila y limpia archivos auxiliares
def limpiar_compilar(nombre, fichero="book", conSecuencia=True):
    limpiar()
    compilar(nombre, fichero, conSecuencia)
    limpiar()


# Compila y limpia todo
def all():
    limpiar_compilar("tesis"),
    limpiar_compilar("paper-i3e", "ieee-paper"),
    limpiar_compilar("presentacion", "presentacion", False)
