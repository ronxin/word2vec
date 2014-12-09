"""Filters vocabulary according to user's specification. 

Usage: $0 < input_vocab > output_vocab
output_vocab = intersection(desired_vocab, input_vocab)
desired_vocab is specified below
"""
import sys

desired = ['king', 'queen', 'man', 'woman', 'his', 'her', 'he', 'she', 'men', 'women']
desired_set = set(desired)

first_line = True

for line in sys.stdin:
  line = line.strip()
  if first_line:
    first_line = False
    print line
    continue
  word, cnt = line.split()
  if word in desired_set:
    print line
