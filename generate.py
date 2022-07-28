# from functions import find
from sys import argv
from functions import *


def build_common(nombre, folder="book"):
    clean(folder)
    build(nombre, folder)
    clean(folder)


def build_presentacion():
    folder = "presentacion"
    clean(folder)
    build_ppt("presentacion", "presentacion")
    clean(folder)

if len(argv) == 1:
    build_common("tesis")
    
elif len(argv) > 1:
    if argv[1] == "clean":
        clean()

    elif argv[1] == "paper":
        build_common("paper-i3e", "ieee-paper")

    elif argv[1] == "ppt":
        build_presentacion()

    elif argv[1] == "all":
        build_common("tesis", "book")
        build_common("paper-i3e", "ieee-paper")
        build_presentacion()

    else:
        build_common(argv[1], argv[2]);
