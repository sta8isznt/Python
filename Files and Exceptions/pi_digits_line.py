filename = 'pi_digits.txt'
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

pi = ''
for line in lines:
    pi += line.strip()

print(pi)
print(len(pi))