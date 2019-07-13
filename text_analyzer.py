import sys
from text_processor import QuerySmallTextFile
# python example_solution.py input_data.txt list_of_commands.txt output.txt

if len(sys.argv) == 4:
  print 'Processing!'
  input_data = sys.argv[1]
  list_of_commands = sys.argv[2]
  output_filepath = sys.argv[3]
  qt = QuerySmallTextFile(input_data, output_filepath)
  qt.process_all_commands(list_of_commands)
else:
  print 'Expecting 3 arguments'