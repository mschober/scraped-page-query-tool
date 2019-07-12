import sys
from text_processor import process_all_commands
# python example_solution.py input_data.txt list_of_commands.txt output.txt

if len(sys.argv) == 3:
  print 'Processing!'
  input_data = sys.argv[1]
  list_of_commands = sys.argv[2]
  #TODO: handle file output
  results = process_all_commands(input_data, list_of_commands)
  print results
else:
  print 'Expecting 2 arguments'