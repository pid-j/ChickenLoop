import zipfile, os
from pathlib import Path

EXTENSIONS: tuple = (".png", ".mp3", "json")
path: Path = Path(__file__).parent.resolve()

if not path.joinpath("project.json").exists():
    raise FileNotFoundError(
        "project.json does not exist in this file's " \
        "parent directory. Are you sure that " \
        "the parent directory is a clone of the " \
        "`src` branch?")

sb3path: Path = path.joinpath("ChickenLoop.sb3")

if sb3path.exists():
    raise FileExistsError(
        "ChickenLoop.sb3 already exists in this" \
        "directory. You do not need to run this " \
        "script if you already have this file. ")

with zipfile.ZipFile(str(sb3path), "w") as file:
    for item in os.listdir(str(path)):
        if "Packager" in item: continue
        if item[-4:] not in EXTENSIONS: continue
        if path.joinpath(item).is_dir(): continue
        file.write(
            str(path.joinpath(item)), item)
        
print("Packaging complete. Enjoy!")