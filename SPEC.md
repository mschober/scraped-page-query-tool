Hi Michael,

 

Thanks for your interest in BrandVerity! We have a coding exercise for you to complete. Out of respect for your time, we ask you to spend no more than two hours completing this exercise.  While we understand that it could be hard to submit something for an interview that you don’t feel is perfect and that you could spend more time to make it perfect, real work isn’t perfect and we want to make reasonable and equal demands on candidates’ time, so please submit what you have at two hours.

 

Please use Python, Java, or C# in mono (we don’t have Windows), whichever you are most comfortable with.  Don’t feel you have to work in Python - we want to see your skills in your strongest language of these. Feel free to use the standard library for the language you choose.

 

One of the challenges we work on at BrandVerity is to analyze text that we've extracted from pages on the internet.  We do this in order to evaluate whether these pages contain information that our customers have told us is relevant to them.  In this spirit, we would like you to build a text analysis program which will process extracted text using a collection of commands that you will implement.  Your program will read a list of analysis commands from a file, and write the resulting output of those commands to a new text file.

 

Input:

A file containing the extracted text.
A file containing a list of commands. Each command is on its own line.
Output:

A file containing the results of each command.  Each result is on its own line.
 

Your implementation should support the following commands: 

 

FREQUENCY term1 term2 term3 ... termN
 

Return space-separated integers indicating how many times each term occurs in the text.
A term should not be counted if it overlaps with other terms, without being separated by a space!
 

IN_ORDER term1 term2 term3 ... termN
 

Return a boolean (“TRUE” or “FALSE”). Return True if terms 1 through N occur in the text in the order specified, even with other terms in between them.
If any one of the terms does not exist in the text, always return FALSE.
If only one term is given, and it exists in the text, always return TRUE.
 

TOP n
 

Return n space-separated terms, sorted by most frequently occurring in the input data. In the case of a tie, prefer the term that comes first alphabetically.
If n is greater than the count of terms in the input data, return all terms from the input data, correctly sorted as above.
If input data is empty, return an empty line 
 

For this exercise, we simply define a “term” as a group of non-whitespace characters separated from other terms by whitespace.  Terms that are provided in the input file as arguments to commands are case-sensitive and punctuation-sensitive; they must match the text exactly. Therefore, your program will not need to modify the arguments to the commands (e.g., change case, remove non-alphanumeric characters or anything similar). A space character is the only delimiter in input lines, so every other character should be regarded as valid input.

 

This program is meant to simulate a tool that our analysts will use on their laptops to run ad hoc debugging queries against web pages that we’ve crawled. They expect that their commands file will process quickly once the program has finished any initial parsing of the page. 

 

We will test your program by executing it from a shell and passing these three command line arguments to it in this order:

A valid path to a text file
A valid path to the commands file
A valid path to an output file 
 

For example:

python example_solution.py input_data.txt list_of_commands.txt output.txt

 

We have attached 3 files as a basic example to help you with your implementation:

An example input text file
An example commands file
An expected output file
 

We expect your solution to produce a new file, identical to the expected output file, when given the example input and commands files.

 

Please include the following in a zip or tar compressed file:

Your source code.
A README file which includes:
An explanation of how quickly each of the commands you implemented will run (time complexity).
An explanation of how much memory your program uses (space complexity).
If your program must be built or compiled, please include detailed step-by-step instructions for how to build your program from the command line. Please be explicit, as we may not be familiar with the build tools.
Detailed instructions on how to run your program from the command line.
Any assumptions, limitations and known issues
 

Good luck and have fun!

 

Andrew