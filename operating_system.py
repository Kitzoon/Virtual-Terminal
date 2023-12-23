import datetime


def get_date():
  return str(datetime.datetime.now()).split(" ")[0]

files = {}

def add_file(file_type, file_name, file_value):
  files[file_type] = {"file_name": str(file_name), "file_data": str(file_value), "creation_date": get_date()}

def find_file(file_name, print_error):  
  for i, file_data in files.items():
    if file_data["file_name"].lower() == file_name:
      return [i, file_data]

  if print_error is True:
    print(
        "Error: file not found (make sure to only enter the name and not the file type)"
    )
  
  return False