"""Create a set of commands to extract the segments into individual .WAVs."""
import os
import sys
import json

def create_script(segments_filename):
  speaker_dict = {}
  with open(segments_filename) as f:
    for line in f:
      segment_id, speaker_id, start_time, end_time = line.strip().split(' ')
      if speaker_id not in speaker_dict:
        speaker_dict[speaker_id] = {}
  for speaker_id in speaker_dict.keys():
    print('python -m datasets.generate_data ../datasets/{0}/alignment.json'.format(speaker_id))

if __name__ == "__main__":
  create_script(sys.argv[1])
