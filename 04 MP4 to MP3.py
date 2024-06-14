import os
import subprocess

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths relative to the script's directory
input_file = os.path.join(script_dir, "input.mp4")
output_file = os.path.join(script_dir, "output.mp3")

def convert_mp4_to_mp3(input_file, output_file):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        output_file
    ]
    subprocess.run(command)

convert_mp4_to_mp3(input_file, output_file)
