# 6.5
text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find(":")+1:].strip()))

# 7.1
fname = input("Enter file name: ")
if (len(fname) < 1): fname = "words.txt"
fh = open(fname)
print(fh.read().upper().rstrip())

# 7.2
fname = input("Enter file name: ")
fname = "mbox-short.txt"
tong = 0
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    tong += float(line[line.find(":")+1:].strip())
    count += 1
print("Average spam confidence:", tong/count)

# 8.4
fname = input("Enter file name: ")
if (len(fname) < 1): fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    sth = line.strip().split()
    for s in sth:
        if s not in lst: lst.append(s)
print(sorted(lst))

# 8.5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        print(line.split()[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")

# 9.4
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
my = dict()
for line in handle:
    if line.startswith("From "):
        email = line.strip().split()[1]
        my[email] = my.get(email, 0) + 1
    max = 0
    mail = None
    for k,v in my.items():
        if max < v:
            max = v
            mail = k
print(mail, max)

# 10.2
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
my = dict()
for line in handle:
    if line.startswith('From '):
        hr = line.strip().split()[-2].split(':')[0]
        my[hr] = my.get(hr, 0) + 1
for k, v in sorted(my.items()):
    print(k, v)
