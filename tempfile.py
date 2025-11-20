from pathlib import Path

class TempFileWriter:
    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.f = self.filepath.open("w")
        print("Fichier créé ")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        self.filepath.unlink()
        print("Fichier supprimé ")


with TempFileWriter() as f:
    f.write("Bonjour depuis le fichier temporaire !\n")
