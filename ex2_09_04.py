fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname, 'r')
di = dict()
list1 = list()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From: "): continue
    line = line[6:]
    words = line.split()
    for w in words:
        di[w] = di.get(w,0) + 1
largest = 0
theword = None
for k,v in di.items():
    if v > largest :
        largest = v
        theword = k
print(theword, largest)
