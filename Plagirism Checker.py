
from difflib import SequenceMatcher 

string1 = 'I am geek'
string2 = 'you are a person'

match = SequenceMatcher(None, 
						string1, string2) 

result = match.ratio() * 100

print(int(result), "%")
