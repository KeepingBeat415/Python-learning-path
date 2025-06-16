 import re

 pattern_1 = re.compile("[a-z]+@[a-z]+.[a-z]+") # create pattern
 pattern_2 = re.compile("[^ ]+@[a-z]+.[a-z]")
 
 matches = pattern.findall(text)

 # [...] Matches a single character or a range that is contained within brackets
 # () Matches an optional expression. EX: (?: com | ca)
"""
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
"""

# ---- extract URLs ----
pattern = re.compile("https?://(?:www.)?[^ ]+\ .com")

# ---- extract IP ----
pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")

# ---- Filtering Files ----
from pathlib import Path

root_dir = Path('files')

filenames = root_dir.iterdir()
filenames_str = [filename.name for filename in filenames]

import re

pattern = re.compile("nov[a-z]*-?:[1-9]|1[0-9]|20.txt", re.IGNORECASE)
matches = [filename for filename in filenames_str if pattern.findall(filename)]

data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com", 
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]

pattern = re.compile("Delhi", re.IGNORECASE)

matches = [str_ for str_ in data if pattern.findall(str_)]

# ---- Files ----
file = open('files/file1.txt', 'w')
file.write('First text\n')

file.close()

with open('file1.txt', 'w') as file:
    file.write('content')
   
content = ''    
with open('file3.csv', 'r') as file:
    content = file.read()
 
content[:-1]