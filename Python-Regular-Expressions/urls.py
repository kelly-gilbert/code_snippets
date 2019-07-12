import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


# match urls
pattern = re.compile('https?://(www\.)?\w+\.\w+')    
matches = pattern.finditer(urls)
for match in matches:
    print(match)


# capture groups
# 1 = optional www, 2 = domain, 3 = top-level domain
pattern = re.compile('https?://(www\.)?(\w+)(\.\w+)')    
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1), match.group(2), match.group(3), sep='\t')


# use capture groups to substitute group2+group3 for the full url
# i.e. remove the optional www
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)



# capture groups
# 1 = optional www, 2 = domain, 3 = top-level domain
pattern = re.compile('https?://(www\.)?(\w+)(\.\w+)')    
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1), match.group(2), match.group(3), sep='\t')
