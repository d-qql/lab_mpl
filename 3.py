import matplotlib.pyplot as plt

f = open('students.csv', 'r')
data = []
for lines in f:
    t = [a for a in lines.split(sep=';')]
    t[1], t[2] = int(t[1]), int(t[2])
    data.append((t[0], t[1], t[2]))

preps, groups = set(), set()
for el in data:
    preps.add(el[0])
    groups.add(el[1])

preps = [a for a in preps]
preps.sort()
groups = [a for a in groups]
groups.sort()

marks = dict.fromkeys(preps, 0)
prevmarks = dict.fromkeys(preps, 0)
fig, ax = plt.subplots(2, figsize=(10,6))

for i in range(3, 11):
    for el in data:
        if el[2] == i:
            marks[el[0]] += 1
    ax[0].bar([a for a in marks.keys()], [a for a in marks.values()], bottom=[a for a in prevmarks.values()], label=f'{i}')
    for p in preps:
        prevmarks[p] += marks[p]
    marks = dict.fromkeys(preps, 0)

ax[0].legend(loc='upper right')

marks = dict.fromkeys(groups, 0)
prevmarks = dict.fromkeys(groups, 0)

for i in range(3, 11):
    for el in data:
        if el[2] == i:
            marks[el[1]] += 1
    ax[1].bar([a for a in marks.keys()], [a for a in marks.values()], bottom=[a for a in prevmarks.values()], label=f'{i}')
    for p in groups:
        prevmarks[p] += marks[p]
    marks = dict.fromkeys(groups, 0)

ax[1].legend(loc='upper right')
plt.show()
