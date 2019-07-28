import re
handle = open('regex_sum_249284.txt')
lst = list()
for line in handle:
    middle = re.findall('[0-9]+', line)
    lst = lst + middle
convert2integers = map(int, lst)
outcome = sum(convert2integers)
print(outcome)
