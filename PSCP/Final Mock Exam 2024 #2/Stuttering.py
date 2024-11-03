'''sss'''
import re

text = input()
ss = re.sub(r'\b(\w+)( \1)+', r'\1', text)
ss = re.sub(r'\s+', ' ', ss).strip()
print(ss)
