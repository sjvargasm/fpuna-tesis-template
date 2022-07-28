from sys import argv
from functions import *


# De acuerdo al parámetro de programa ejecuta una compilación en concreto
if len(argv) == 1:
    limpiar_compilar("tesis")
elif len(argv) > 1:
    if argv[1] == "clean":
        limpiar()
    elif argv[1] == "paper":
        limpiar_compilar("paper-i3e", "ieee-paper")
    elif argv[1] == "ppt":
        limpiar_compilar("presentacion", "presentacion", False)
    elif argv[1] == "all":
        limpiar_compilar("tesis")
        limpiar_compilar("paper-i3e", "ieee-paper")
        limpiar_compilar("presentacion", "presentacion", False)
    else:
        limpiar_compilar(argv[1])  # TODO: Hacer que funcione?
