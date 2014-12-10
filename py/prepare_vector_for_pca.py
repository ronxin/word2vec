"""Prepares a text-format word2vec vectors for R's PCA.

Usage: $0 input-vectors.txt output-vectors.txt
"""
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

k = 0
V = 0
with open(output_file, 'w') as fout:
  with open(input_file, 'r') as fin:
    first_line = True
    count = 0
    for line in fin:
      line = line.strip()
      if first_line:
        first_line = False
        V, k = line.split()
        V = int(V)
        k = int(k)
        continue
      fs = line.split()
      if fs[0] == '</s>':
        V -= 1
        continue
      assert len(fs) == k + 1
      fout.write('"' + fs[0] + '"\t')
      fout.write('\t'.join(fs[1:]))
      fout.write('\n')
      count += 1
      if count == V:
        break
assert count == V
print 'Done'
