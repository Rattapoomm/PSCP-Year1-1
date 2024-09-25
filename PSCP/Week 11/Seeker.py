'''seeker'''
import re
text = input()
numbers = [int(num) for num in re.findall(r'\d+', text)]
total = sum(numbers)
print(total)
