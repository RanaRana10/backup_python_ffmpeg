import subprocess

def merge_videos(input_video1, input_video2, output_video):
    cmd = [
        'ffmpeg',
        '-i', input_video1,
        '-i', input_video2,
        '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[outv][outa]',
        '-map', '[outv]',
        '-map', '[outa]',
        output_video
    ]

    subprocess.run(cmd)

# Example usage
merge_videos('v1.mp4', 'v2.mp4', 'output.mp4')
