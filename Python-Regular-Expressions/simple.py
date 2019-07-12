import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


# re.compile allows you to save the pattern to a variable
# r'string' is a raw string (literal interpretation)
# this is important because you may need to use backslashes to escape
#pattern = re.compile(r'\.')
pattern = re.compile(r'\b')

# matches is an iterator that contains all of the matches of pattern
matches = pattern.finditer(text_to_search)

# iterate through the matches
for match in matches:
    print(match)
    

print(text_to_search[1:4])



# word boundaries
text_to_search2 = 'abc def ghijkl '
pattern = re.compile(r'\b')
matches = pattern.finditer(text_to_search2)

for match in matches:
    print(match)
 
    
# match phone numbers
pattern = re.compile('\d{3}.\d{3}.\d{4}')    
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# read in a file of contact info and find all of the phone numbers
with open('data.txt', 'r') as f:
    contents = f.read()
    
pattern = re.compile('\d{3}.\d{3}.\d{4}')    
matches = pattern.finditer(contents)
for match in matches:
    print(match)
    

# only match a specific character set (dash or a dot between numbers)
pattern = re.compile('\d{3}[-.]\d{3}[-.]\d{4}')    
matches = pattern.finditer(contents)
for match in matches:
    print(match)


# only match 800- and 900- numbers
pattern = re.compile('[89]00[-.]\d{3}[-.]\d{4}')    
matches = pattern.finditer(contents)
for match in matches:
    print(match)



# only match numbers 1 through 5
pattern = re.compile('[1-5]')    
matches = pattern.finditer(contents)
for match in matches:
    print(match)


# only match numbers ucase or lcase a-e
pattern = re.compile('[A-Ea-e]')    
matches = pattern.finditer(contents)
for match in matches:
    print(match)


# findall method (similar to finditer, except it just returns the matching text
# and not a match object
pattern = re.compile('\d{3}.\d{3}.\d{4}')    
matches = pattern.findall(contents)
for match in matches:
    print(match)


# match method: finds a match at the start of the string and returns 
# the match object
# (or None if there is no match)
pattern = re.compile(r'Start')    
matches = pattern.match(sentence)
print(matches)


# search method: same as match, except finds first match anywhere within the string
# (or None if there is no match)
pattern = re.compile(r'1234')    
matches = pattern.search(text_to_search)
print(matches)


# flags
pattern = re.compile(r's', re.IGNORECASE)    
matches = pattern.finditer(sentence)
for match in matches:
    print(match)




pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)
