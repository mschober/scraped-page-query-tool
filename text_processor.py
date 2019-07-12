
def read_commands(list_of_commands):
  commands_list = []
  with(open(list_of_commands, 'r')) as f:
    command = f.readline()
    while command:
      commands_list.append(command)
      command = f.readline()
  return commands_list

def process_all_commands(input_data, list_of_commands):
  commands_list = read_commands(list_of_commands)
  print 'going to scrape!', commands_list