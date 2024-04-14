import os
from moviepy.editor import VideoFileClip


def trim_video(video_file, output_file, trim_end_time, predicate=lambda x: True):
    """Trim a video file using a predicate function."""
    video_clip = VideoFileClip(video_file)

    if predicate(video_clip.duration):
        start_time = video_clip.duration - trim_end_time
        trimmed_video_clip = video_clip.subclip(start_time, video_clip.duration)

        trimmed_video_clip.write_videofile(output_file)
        video_clip.close()


def trim_all(input_path, output_path, trim_end_time=20):
    """Trim all files in a directory, excluding videos shorter than trim_end_time. + x seconds"""
    for file in os.listdir(input_path):
        if file.endswith(".mp4"):
            input_file = os.path.join(input_path, file)
            output_file = os.path.join(output_path, file)
            trim_video(input_file, output_file, trim_end_time, predicate=lambda x: x > trim_end_time + 10)


directory = "F:\\your\\videos\\path"  # Change to your desired directory
input_folder = os.path.join(directory, "videos")  # Change to your video folder
output_folder = os.path.join(input_folder, "trimmed")  # Change to your trimmed folder
end_time = 15  # Change your desired clip length

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

trim_all(input_folder, output_folder, end_time)
