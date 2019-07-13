import operator
def process_frequency_command(input_data, args):
  '''
  1. Reads the text from the input data.
  2. Loops over each word in text
  '''

  def fill_freq_request_map(args):
    '''
    1. Fills a request map for each word to track frequency on.
    '''
    freq_req_map = {}
    pos = 0
    for arg in args:
      if arg in freq_req_map: 
        freq_req_map[arg].append(pos)
        pos += 1
      else:
        freq_req_map[arg] = [pos]
        pos += 1
    return freq_req_map
  count_requests = len(args)
  freq_req_map = fill_freq_request_map(args)

  def read_text(input_data):
    '''
    1. Reads the lines of text from the file and splits into tokens.
    '''
    text = None
    with(open(input_data)) as f:
      text = f.read().split()
    return text

  def count_word_freq(text, freq_req_map):
    '''
    1. 
    '''
    freq_map = {}
    for word in text:
      if word in freq_req_map:
        if word in freq_map:
          freq_map[word] += 1
        else:
          freq_map[word] = 1
    return freq_map

  print 'Start frequency command'
  text = read_text(input_data)
  freq_map = count_word_freq(text, freq_req_map)

  #TODO: need to figure out how to increment pos if a request word isn't found anywhere in the text
  for word in freq_req_map:
    if not word in freq_map:
      print word
      freq_map[word] = 0
      
  # print text
  # print "freq_req_map", freq_req_map
  # print len(freq_req_map)
  # print "freq_map", freq_map

  to_print = ''
  freqs = [None]*count_requests
  for req in sorted(freq_req_map.items(), key=operator.itemgetter(1)):
    freq = freq_map[req[0]]
    positions = req[1]
    for pos in positions:
      # print "update pos", pos
      freqs[pos] = str(freq)
  print ' '.join(freqs)
def process_top_command(input_data, args):
  print 'Start top command'
def process_inorder_command(input_data, args):
  print 'Start inorder command'



def process_all_commands(input_data, list_of_commands):
  '''
  1. Loops over all the commands and splits them into a command type and a list of arguments.
  2. Maps command types to methods to run the command on the input data.
  3. Aggregates the results from all commands and returns the results.
  '''
  results = []
  for command in open(list_of_commands):
    split_command = command.rstrip().split(' ')
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
  return results