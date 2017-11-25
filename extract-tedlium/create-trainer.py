"""Create a set of commands to extract the segments into individual .WAVs."""
import os
import sys
import json

with open('processed.txt') as f:
  processed = ['../datasets/{0}'.format(l.strip()) for l in f]

print('python3 train.py --data_path={0}'.format(','.join(processed[:5])))

