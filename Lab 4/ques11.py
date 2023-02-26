lis = list(map(int, input('Enter list elements: ').split())) freq = {}
for i in lis:
if i in freq: freq[i] += 1
else:
freq[i] = 1 revFreq = {} ans = []
for f in freq:
if freq[f] not in revFreq: revFreq[freq[f]] = [f]
else:
revFreq[freq[f]].append(f) set1 = set()
