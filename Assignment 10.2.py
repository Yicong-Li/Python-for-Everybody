name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        dic[time[0]] = dic.get(time[0], 0) + 1
outcome = sorted(dic.items())
for k, v in outcome:
    print(k, v)