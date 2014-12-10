"""Reads in the text-format vectors, takes in a three-word query, and use 2 different methods to solve analogy. Prints out detailed information."""
# NOTE: the vectors output by word2vec are normalized yet. distance.c normalizes it. So here I should normalize it by hand, too.
# Usage: $0 vectors.txt
 
import sys
import math

k = 0  # number of dimension
V = 0  # size of vocabulary
vec = {}

print 'Reading input...'

def vec_len(a):
  return math.sqrt(sum([x*x for x in a]))

def normalize(a):
  vlen = vec_len(a)
  return [x/vlen for x in a]

with open(sys.argv[1], 'r') as fin:
  first_line = True
  for line in fin:
    line = line.strip()
    if first_line:
      V, k = line.split()
      V = int(V)
      k = int(k)
      first_line = False
      continue
    fs = line.split()
    assert len(fs) == k + 1
    word = fs[0]
    if word == "</s>":
      V -= 1
      continue
    assert not word in vec
    new_vec = [float(x) for x in fs[1:]]
    new_vec = normalize(new_vec)
    assert len(new_vec) == k
    vec[word] = new_vec
    if V == len(vec):
      # avoid reading any output vectors (if any) 
      break

# between -1 and 1 (for unit-length vectors)
def inner(a, b):
  assert len(a) == len(b)
  out = 0.0
  for i in range(len(a)):
    out += a[i] * b[i]
  return out

# between 0 and 1
def pos_inner(a, b):
  return (inner(a, b) + 1.0) / 2 

# cos(w1 - w2, w3 - w4)
def pair_direction(w1, w2, w3, w4):
  assert len(w1) == len(w2)
  assert len(w2) == len(w3)
  assert len(w3) == len(w4)
  out = 0.0
  for i in range(len(w1)):
    out += (w1[i] - w2[i]) * (w3[i] - w4[i])
  return out 

while True:
  line = raw_input('Type three word (e.g., man king queen; EXIT to exit): ')
  line = line.strip()
  if line == 'EXIT':
    break
  fs = line.split()
  if len(fs) != 3:
    continue
  
  words = fs
  should_break = False
  for word in words:
    if not word in vec:
      should_break = True
      print '"' + word + '" is not in dictionary.'
      break
  if should_break:
    break
  
  # candidates
  cand = {}
  colnames = ['candidate', words[0], words[1], words[2], '3COS', '3COSMult', 'PairDir']
  for word in vec:
    if word in words:
      continue
    new_cand = []
    three_cos = 0.0
    three_cos_mult = 1.0
    for i, w in enumerate(words):
      pin = pos_inner(vec[word], vec[w])  # positive inner product
      # debug
      if pin > 1:
        print word, inner(vec[word], vec[word]), w, inner(vec[w], vec[w])
        sys.exit()
      new_cand.append(pin)
      if i == 1:
        three_cos -= pin
        three_cos_mult /= (pin + 1e-6)
      else:
        three_cos += pin
        three_cos_mult *= pin
    assert len(new_cand) == 3
    new_cand.append(three_cos)
    new_cand.append(three_cos_mult)
    assert len(new_cand) == 5
    pair_dir = pair_direction(vec[words[0]], vec[word], vec[words[1]], vec[words[2]])
    new_cand.append(pair_dir)
    assert len(new_cand) == 6
    assert len(new_cand) == len(colnames) - 1
    cand[word] = new_cand
  
  # output
  print '\t'.join(colnames)
  for c in cand:
    print '\t'.join([c] + [str(x) for x in cand[c]])
  
 