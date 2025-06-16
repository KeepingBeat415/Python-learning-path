from pathlib import Path
from datetime import datetime
import zipfile

path1 = Path('scrap_msg.txt')

if path1.exists():
    with open(path1, 'r') as file:
        print(file.read())


root_dir = Path('files')
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new+" + path.stem + path.suffix
    #print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

## recursvie into sub-folder
file_paths_2 = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        print(path)
        new_filename = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)

path3 = Path('files/Dec/jkl.txt')
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromatimestamp(second_created)
# output as: 2025-06-02 16:03:33
date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")


# modify file's extension
file_paths_3 = root_dir.rglob("*.txt")
for path in file_paths:
    if path.is_file():
        new_filepath = path.with_suffix('.csv')
        path.rename(new_filepath)


root_dir = Path('files')
# create files from loop
for i in range(10, 21):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

# create archive zip
with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink() ## delete files

root_dir = Path('files')
destination_path = Path('files/Des')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_path / Path(path.stem)
        zf.extractall(path=final_path)


# ---- Down Files ----
url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

import requests

req = requests.get(url)

 with open('download.map3', 'wb') as file:
     file.write(req)
     
# ---- Upload Files ----
url = 'https://cgi-lib.berkerley.edu/ex/fup.cgi'

file = open('myfile.txt', 'rb')

req = requests.post(url, file={"upfile":file})

print(req.text)

