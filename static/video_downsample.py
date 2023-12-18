import os
import subprocess

def convert_videos(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith((".mp4", ".avi", ".mkv")):  
                filepath = os.path.join(root, filename)
                output_path = os.path.join(root, "converted_" + filename)

                cmd = f"ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 \"{filepath}\""
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                current_bitrate = int(result.stdout.strip())

                if current_bitrate > 2000:
                    print(f"Converting {filename}...")
                    cmd = f"ffmpeg -i \"{filepath}\" -b:v 2000k \"{output_path}\""
                    subprocess.run(cmd, shell=True)

convert_videos('./videos/')  
