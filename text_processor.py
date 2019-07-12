def processAllCommands(input_data, commands):
  commands_list = []
  command = '<placeholder>'

  with(open(commands, 'r')) as f:
    command = f.readline()
    while command:
      commands_list.append(command)
      command = f.readline()
  print 'going to scrape!', commands_list