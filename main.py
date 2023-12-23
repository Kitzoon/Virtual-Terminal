from commands import commands
from operating_system import add_file


def input_command(command):
  formattedCommand = command.split()[0].lower()

  if formattedCommand in commands and "callback_function" in commands[
      formattedCommand]:
    command_callback = commands[formattedCommand]["callback_function"]
    args = command.split()[1:]

    if args and commands[formattedCommand]["needs_arguments"] is True:
      command_callback(args)
    else:
      if commands[formattedCommand]["needs_arguments"] is False:
        command_callback()
      elif commands[formattedCommand]["needs_arguments"] is True:
        print("Error: This command requires arguments")
  else:
    print("Error: Command not found")

  input_command(input("> "))


add_file("txt", "Introduction", "Welcome to VirtualTerminal!")

print("VirtualTerminal - Type 'help' for a list of commands\n\n")

input_command(input("> "))
