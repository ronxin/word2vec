# Get a list of unique words from vocabulary.
# Usage: $0 < INPUT > OUTPUT
import sys
words  = {}
for line in sys.stdin:
  line = line.strip()
  if line[0] == ':':
    continue
  fs = line.split()
  assert len(fs) == 4
  for w in fs:
    words[w] = 1

for w in words:
  print w

