import subprocess

def merge_videos(input_video1, input_video2, output_video):
    cmd = [
        'ffmpeg',
        '-i', input_video1,
        '-i', input_video2,
        '-filter_complex', '[0:v]scale=1280x800[v1];[1:v]scale=1280x800[v2];[v1][0:a][v2][1:a]concat=n=2:v=1:a=1[outv][outa]',
        '-map', '[outv]',
        '-map', '[outa]',
        output_video
    ]

    subprocess.run(cmd)

# Example usage
input1 = 'v1.mp4'
input2 = 'v2.mp4'
output = 'v1 And v2.mp4'


merge_videos(input1, input2, output)
