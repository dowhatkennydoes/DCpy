# Import the required method
from zipfile import ZipFile

with ZipFile(path, mode="r") as f:
  	# Get the list of files and print it
    file_names = f.namelist()
    print(file_names)