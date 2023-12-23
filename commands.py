from operating_system import files, add_file, get_date, find_file

commands = {}


def new_command(name, description, callback_function, needs_arguments):
  commands[name] = {
      "description": description,
      "callback_function": callback_function,
      "needs_arguments": needs_arguments
  }


def ls_callback():
  count = 0

  for file_type, file_data in files.items():
    count += 1
    print(f"{count} - {file_data['file_name']}.{file_type}")

  if count == 0:
    print("No files found")


new_command("ls", "List files", ls_callback, False)


def help_callback():
  for command_name, command_data in commands.items():
    print(f"{command_name} - {command_data['description']}")


new_command("help", "List avaliable commands", help_callback, False)


def read_callback(args):
  file_name = str(args[0]).lower()

  file = find_file(file_name, True)

  if file is not False:
    file_data = file[1]
    print(file_data["file_data"])


new_command("read", "Read a file's data", read_callback, True)


def create_callback(args):
  file_name = str(args[0]).lower()
  file_type = str(args[1]).lower()

  file = find_file(file_name, False)

  if file is not False:
    print("Error: A file with that name already exists")
    return

  add_file(file_type, file_name, "")
  print(f"Created file {file_name}.{file_type}")


new_command("create", "Create a new file", create_callback, True)


def delete_callback(args):
  file_name = str(args[0]).lower()
  file = find_file(file_name, True)

  if file is not False:
    file_type = file[0]
    
    confirm = input(
        "Are you sure you want to delete this file? It cannot be recovered. (y/n) "
    ).lower()

    if confirm == "y":
      files.pop(file_type)
      print(f"Deleted file {file_name}.{file_type}")


new_command("delete", "Delete's a file", delete_callback, True)


def edit_callback(args):
  file_name = str(args[0]).lower()

  file = find_file(file_name, True)

  if file is not False:
    file_type = file[0]
    file_data = file[1]

    if file_data["file_data"] != "":
      confirm = input(
          "Are you sure you want to edit this file? All previous data on it will be removed. (y/n) "
      ).lower()

      if confirm == "y":
        new_data = input(f"Enter the new data for {file_name}.{file_type}: ")
        file_data["file_data"] = str(new_data)
        print(f"Edited file {file_name}.{file_type}")
      else:
        print(f"Cancelling the edit for {file_name}.{file_type}")
    else:
      new_data = input(f"Enter the new data for {file_name}.{file_type}: ")
      file_data["file_data"] = str(new_data)
      print(f"Edited file {file_name}.{file_type}")


new_command("edit", "Edit a file's data", edit_callback, True)


def python_callback(args):
  file_name = str(args[0]).lower()
  file = find_file(file_name, True)

  if file is not False:
    file_data = file[1]
    exec(str(file_data["file_data"]))


new_command("python", "Run python through a file's data", python_callback,
            True)


def date_callback():
  print("Current date: " + get_date())


new_command("date", "Get the date", date_callback, False)


def info_callback(args):
  file_name = str(args[0]).lower()

  file = find_file(file_name, True)

  if file is not False:
    file_type = file[0]
    file_data = file[1]

    print(f"File Name: {file_data['file_name']}")
    print(f"File Type: {file_type}")
    print(f"File created in: {file_data['creation_date']}")


new_command("info", "Get information about a file", info_callback, True)
