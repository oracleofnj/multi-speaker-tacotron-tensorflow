"""Create a set of commands to extract the segments into individual .WAVs."""
import os
import sys

def create_script(segments_filename, sph_path, output_path):
  with open(segments_filename) as f:
    for line in f:
      segment_id, file_id, start_time, end_time = line.strip().split(' ')
      dest_path = os.path.join(output_path, file_id, 'audio')
      os.makedirs(dest_path, exist_ok=True)
      print('sph2pipe -f wav -t {0}:{1} -p {2}.sph > {3}.wav'.format(
            start_time, end_time,
            os.path.join(sph_path, file_id),
            os.path.join(dest_path, segment_id)
      ))

if __name__ == "__main__":
  create_script(sys.argv[1], sys.argv[2], sys.argv[3])

