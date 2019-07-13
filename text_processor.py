import operator

class QuerySmallTextFile:
  '''
  By wrapping the output file handle methods can write results and not worry about file I/O.
  By reading all the text into memory, subsequent queries don't have to read the original text file.
  NOTE: If the input file got large, this in memory solution wouldn't be sufficient.
  '''
  def __init__(self, input_data_filepath, output_data_filepath):
    self.output_file = open(output_data_filepath, 'w')
    self.text = self.read_file(input_data_filepath)
    
  def read_file(self, input_file):
    '''
    1. Reads the lines of text from the file and splits into tokens.
    '''
    text = None
    with(open(input_file, 'r')) as f:
      text = f.read().split()
    return text

  def process_all_commands(self, list_of_commands):
    '''
    1. Loops over all the commands and splits them into a command type and a list of arguments.
    2. Maps command types to methods to run the command on the input data.
    3. Writes results to an output file during each call.
    4. Handles file I/O and closes output file if error.
    '''
    #TODO: wrap file handle in a class for handling
    # output_file = open(output_filepath, 'w')
    try:
      for command in open(list_of_commands):
        split_command = command.rstrip().split(' ')
        command_type = split_command[0]
        args = split_command[1:]
        print "DEBUG: ", command_type, args
        if command_type == 'FREQUENCY':
          self.process_frequency_command(args)
        elif command_type == 'TOP':
          self.process_top_command(args)
        elif command_type == 'IN_ORDER':
          self.process_inorder_command(args)
        else:
          raise Exception('Error: unknown command type {}'.format(command_type))
    except:
      self.output_file.close()
    self.output_file.close()
    print 'Done!'

  def process_frequency_command(self, args):
    '''
    1. Loops over frequency requests and populates a map to check during processessing.
    2. Loops over each word in text checking if the word is in the freq request map.
    3. Collates the results so the frequencies are reported against the original requests in the order they were requested.
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
 
    def count_word_freq(text, freq_req_map):
      '''
      1. Loops over all the words in text checking the frequency request map.
      2. If the word is in the request map, then frequency map item is added. 
         If the word was already there the frequence is increased.
      3. If the request wasn't found, a 0 is added to the freq_map.
      '''
      def loop_and_count(freq_req_map):
        freq_map = {}
        for word in text:
          if word in freq_req_map:
            if word in freq_map:
              freq_map[word] += 1
            else:
              freq_map[word] = 1
        return freq_map
      def add_not_found_entries(freq_map, freq_req_map):
        for word in freq_req_map:
          if not word in freq_map:
            print word
            freq_map[word] = 0
        return freq_map
      freq_map = loop_and_count(freq_req_map)
      freq_map = add_not_found_entries(freq_map, freq_req_map)
      return freq_map

    print 'Start frequency command'
    text = self.text
    print 'DEBUG:', text
    count_requests = len(args)
    freq_req_map = fill_freq_request_map(args)
    freq_map = count_word_freq(text, freq_req_map)
        
        
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
    freq_responses = ' '.join(freqs)
    print freq_responses
    self.output_file.write(freq_responses + "\n")

  def process_top_command(self, args):
    print 'Start top command'
  def process_inorder_command(self, args):
    print 'Start inorder command'