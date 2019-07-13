import sys
from text_processor import QueryText
# python example_solution.py input_data.txt list_of_commands.txt output.txt

if len(sys.argv) == 3:
  print 'Processing!'
  input_data = sys.argv[1]
  list_of_commands = sys.argv[2]
  #TODO: handle file output
  qt = QueryText(input_data, './output.txt')
  qt.process_all_commands(list_of_commands)
else:
  print 'Expecting 2 arguments'