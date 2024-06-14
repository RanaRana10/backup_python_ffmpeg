import subprocess

def convert_mp4_to_mp3(input_file, output_file):
    command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file]
    subprocess.run(command)

# Example usage
convert_mp4_to_mp3("input.mp4", "output.mp3")
