# Input: w2v formatted vocab
# Output: w2v formatted vocab (all words lower-cased, removed duplicates)
import sys

writer = open('/storage4/users/ronxin/word2vec/output/vocab-wiki-5gram-200k-lowered', 'w')
seen = {}  # [word] = 1
with open('/storage4/users/ronxin/word2vec/output/vocab-wiki-5gram-200k', 'r') as reader:
  linecount = 0
  for line in reader:
    line = line.strip()
    linecount += 1
    if linecount == 1: writer.write(line + '\n')
    else:
      fs = line.split(' ')
      assert len(fs) == 2
      w = fs[0].lower()
      count = fs[1]
      if not w in seen:
        seen[w] = 1
        writer.write('%s %s\n'%(w,count))

writer.close()
print 'Done'


