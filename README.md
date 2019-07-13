# Scrapped Page Query Tool
> Given a scrapped page of text, allows the user to run various queries about the properties of the text. 
For example frequency of occurrence for a given term. Multiple terms can be supplied for an individual query.
Multiple queries can be sent as a command file.


## Usage
```sh
python text_analyzer.py testcase0/input.txt testcase0/commands.txt $(date +%s)-output.txt
```

## Format

### input.txt
> Should be from "the scrapping tool".

### commands.txt
> One query request per line.

#### Commands supported
* FREQUENCY
* TOP
* IN_ORDER

##### FREQUENCY
```
FREQUENCY term1 term2 term3 ... termN
 

Return space-separated integers indicating how many times each term occurs in the text.
A term should not be counted if it overlaps with other terms, without being separated by a space!
```

##### TOP
```
TOP n
 

Return n space-separated terms, sorted by most frequently occurring in the input data. In the case of a tie, prefer the term that comes first alphabetically.
If n is greater than the count of terms in the input data, return all terms from the input data, correctly sorted as above.
If input data is empty, return an empty line 
```

##### IN_ORDER
```
IN_ORDER term1 term2 term3 ... termN
 

Return a boolean (“TRUE” or “FALSE”). Return True if terms 1 through N occur in the text in the order specified, even with other terms in between them.
If any one of the terms does not exist in the text, always return FALSE.
If only one term is given, and it exists in the text, always return TRUE.
```