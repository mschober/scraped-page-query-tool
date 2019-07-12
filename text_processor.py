def process_frequency_command(input_data, args):
  print 'Start frequency command'
def process_top_command(input_data, args):
  print 'Start top command'
def process_inorder_command(input_data, args):
  print 'Start inorder command'


def process_all_commands(input_data, list_of_commands):
  results = []
  for command in open(list_of_commands):
    split_command = command.split(' ')
    command_type = split_command[0]
    args = split_command[1:]
    print command_type, args
    if command_type == 'FREQUENCY':
      result = process_frequency_command(input_data, args)
    elif command_type == 'TOP':
      result = process_top_command(input_data, args)
    elif command_type == 'IN_ORDER':
      result = process_inorder_command(input_data, args)
    else:
      raise Exception('Error: unknown command type {}'.format(command_type))
    results.append(result)
  print 'Done!'