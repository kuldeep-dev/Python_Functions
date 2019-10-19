# Regular Expressions in Python

import re

mystr = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# findall , search, split , sub, finditer Functions in Regular Expressions

# finditer

pattren = re.compile(r'.ing')
pattren = re.compile(r'^lorem')
pattren = re.compile(r'$lorem')
pattren = re.compile(r'lorem$')
pattren = re.compile(r'a*i*')
pattren = re.compile(r'ai{2}')
pattren = re.compile(r'(ai){2}')
pattren = re.compile(r'ai{1}|t')
pattren = re.compile(r'ai{1}|fax')

# Special sequence
pattren  = re.compile(r'\AFata')
pattren  = re.compile(r'\bFata')
pattren  = re.compile(r'Fata\b')

# digit

pattren = re.compile(r'\d{5}-\d{4}')


matches = pattren.finditer(mystr)

for match in matches:
    print(match)
    # print(mystr[448:442])
