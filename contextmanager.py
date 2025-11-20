from pathlib import Path
from contextlib import contextmanager

@contextmanager
def temp_file():
    path = Path("temp.txt")
    f = path.open("w")
    print("Fichier créé ")
    try:
        yield f
    finally:
        f.close()
        path.unlink()
        print("Fichier supprimé ")

# Test
with temp_file() as f:
    f.write("Écrit via contextmanager !\n")
