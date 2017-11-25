"""Create a set of commands to extract the segments into individual .WAVs."""
import os
import sys
import json

def create_script(segments_filename, text_filename, output_path):
  speaker_dict = {}
  segment_dict = {}
  with open(text_filename) as f:
    for line in f:
      words = line.strip().split(' ')
      segment_dict[words[0]] = ' '.join(words[1:])
  with open(segments_filename) as f:
    for line in f:
      segment_id, speaker_id, start_time, end_time = line.strip().split(' ')
      if speaker_id not in speaker_dict:
        speaker_dict[speaker_id] = {}
      wav_file = '{0}.wav'.format(os.path.join(output_path, speaker_id, 'audio', segment_id))
      speaker_dict[speaker_id][wav_file] = [segment_dict[segment_id]]
  for speaker_id, segments in speaker_dict.items():
    dest_path = os.path.join(output_path, speaker_id)
    with open(os.path.join(dest_path, 'alignment.json'), 'w') as f:
      json.dump(segments, f)

if __name__ == "__main__":
  create_script(sys.argv[1], sys.argv[2], sys.argv[3])

