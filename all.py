d = {}
with open('3.txt') as third:
    a = {}
    b = []
    count = 0
    for line in third:
        b.append(line.strip())
        count += 1
    a[count] = b
    d['3.txt'] = a
with open('2.txt') as second:
    a = {}
    b = []
    count = 0
    for line in second:
        b.append(line.strip())
        count += 1
    a[count] = b
    d['2.txt'] = a
with open('1.txt') as first:
    a = {}
    b = []
    count = 0
    for line in first:
        b.append(line.strip())
        count += 1
    a[count] = b
    d['1.txt'] = a

with open ('summary.txt', 'w', encoding='utf-8') as summary:
    for file, text in d.items():
        for count, value in sorted(text.items(), reverse=True):
            summary.write(file + '\n')
            summary.write(str(count) + '\n')
            for i in value:
                summary.write(i + '\n')


