from contextlib import ExitStack

paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w")) for p in paths]
    print("Tous les fichiers  ouverts ")

    for f in files:
        f.write("Salut \n")

print("écriture  terminée  (tous les fichiers sont fermés automatiquement)")
