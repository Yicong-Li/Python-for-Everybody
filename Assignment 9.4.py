name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        dic[words[1]] = dic.get(words[1], 0) + 1
maxkey = 0
maxvalue = 0
for key, value in dic.items():
    if value > maxvalue:
        maxkey = key
        maxvalue = value
print(maxkey, maxvalue)