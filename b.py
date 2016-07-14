#!/usr/bin/python

import sys

s = ('_').join(sys.argv[1:])
punc = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~'
exclude = set(punc)
s = "B_" + ''.join(ch for ch in s if ch not in exclude)
print s

