from sys import argv
from functions import *


# De acuerdo al parámetro de programa ejecuta una compilación en concreto
if len(argv) == 1:
    cleanbuild("tesis")
elif len(argv) > 1:
    if argv[1] == "clean":
        clean()
    elif argv[1] == "paper":
        cleanbuild("paper-i3e", "ieee-paper")
    elif argv[1] == "ppt":
        cleanbuild("presentacion", "presentacion", False)
    elif argv[1] == "all":
        cleanbuild("tesis")
        cleanbuild("paper-i3e", "ieee-paper")
        cleanbuild("presentacion", "presentacion", False)
    else:
        cleanbuild(argv[1])  # TODO: Hacer que funcione?
