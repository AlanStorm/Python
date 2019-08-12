"""
findall
"""
import re

pattern = re.compile(r'\d+')

s = pattern.findall('u am 18 years old and 185 height')

print(s)

s = pattern.finditer('u am 18 years old and 185 height')

print(type(s))
for i in s:
    print(i.group())
