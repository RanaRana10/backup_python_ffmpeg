import subprocess

def convert_avi_to_mp4(input_avi, output_mp4):
    cmd = [
        'ffmpeg',
        '-i', input_avi,
        '-c:v', 'libx264',  # Use H.264 video codec
        '-c:a', 'aac',  # Use AAC audio codec
        '-strict', 'experimental',
        output_mp4
    ]

    subprocess.run(cmd)

# Example usage
convert_avi_to_mp4('aaa.avi', 'output_video.mp4')
