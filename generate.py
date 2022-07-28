from sys import argv
from functions import *

switcher = {
    "": lambda: limpiar_compilar("tesis"),
    "tesis": lambda: limpiar_compilar("tesis"),
    "b": lambda: limpiar_compilar("tesis"),

    "all": lambda: all(),
    "a": lambda: all(),

    "ppt": lambda: limpiar_compilar("presentacion", "presentacion", False),
    "d": lambda: limpiar_compilar("presentacion", "presentacion", False),

    "paper": lambda: limpiar_compilar("paper-i3e", "ieee-paper"),
    "p": lambda: limpiar_compilar("paper-i3e", "ieee-paper"),

    "clean": lambda: limpiar(),
    "c": lambda: limpiar(),
}

if len(argv) > 1:
    switcher.get(argv[1], lambda: limpiar_compilar(argv[1]))()
else:
    switcher.get("")()