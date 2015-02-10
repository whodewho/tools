import sys
pattern = sys.argv[1]
filename  = sys.argv[2]

care = set([])
with open(filename) as f:
	for line in f:
		if pattern in line:
			care.add(line[:5])

with open(filename) as f:
	for line in f:
		if line[:5] in care:
			print line[:len(line)-1]

