"""Filters vocabulary according to user's specification. 

Usage: $0 input_vocab output_file_prefix
output_vocab = intersection(desired_vocab, input_vocab)
desired_vocab is specified below
"""
import sys

input_file = sys.argv[1]
output_prefix = sys.argv[2]

desired = ['king queen man woman his her he she men women', 
           'king queen man woman prince emperor ruler monarch nobles royal',
           'king queen man woman brother sister father mother son daughter',
           'king queen man woman he his him men himself brother',
           'king queen man woman she her hers women herself sister',
           'Beijing China Seoul Korea Tokyo Japan Taipei Taiwan Moscow Russia',
           'Beijing China Seoul Korea capital city government country Shanghai Busan',
           'king queen man woman musculine feminine stepfather stepmother grandson granddaughter',
           'think thinking read reading thought thinks reads writes write writing',
           'think thinking read reading perception understand expect suspect written copied learning talking',
           'think thinking read reading do does did doing is was']
desired_set = [set(x.split()) for x in desired]

fi = open(input_file, 'r')
fo = [open(output_prefix + str(x), 'w') for x in range(len(desired))]
seen = [set() for x in range(len(desired))]
for line in fi:
  line = line.strip()
  word, cnt = line.split()
  for i in range(len(desired)):
    if word in desired_set[i]:
      fo[i].write(line + '\n')
      seen[i].add(word)

fi.close()
for f in fo:
  f.close()

for i in range(len(desired)):
  for w in desired_set[i]:
    if not w in seen[i]:
      print 'Unseen word for list %d: %s'%(i, w)

print 'Done.'

