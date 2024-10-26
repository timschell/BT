import re
pattern = re.compile(r'\d+')
print(pattern.findall('There are 123 apples and 45 oranges.'))
