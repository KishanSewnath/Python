s = '''It was the best of times, it was the wordt of times; it was the age of wisdom, it was the age of foolishness; it was the epoch of belief, it was the epoch of incredulity; it was ...'''
newS = s.maketrans('.,;\n', '    ')
newS1 = str(s.translate(newS))
newS1 = newS1.replace('  ', ' ')
newS1 = newS1.lower()
count = newS1.count('it was')
print (type(newS))
print(newS1)
print(count)
