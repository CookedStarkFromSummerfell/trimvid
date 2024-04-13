import os
from moviepy.editor import VideoFileClip


def trim_video(video_file, output_file, trim_end_time):
    video_clip = VideoFileClip(video_file)
    start_time = video_clip.duration - trim_end_time
    trimmed_video_clip = video_clip.subclip(start_time, video_clip.duration)

    trimmed_video_clip.write_videofile(output_file)

    video_clip.close()


def trim_all(input_path, output_path, trim_end_time=20):
    for file in os.listdir(input_path):
        if file.endswith(".mp4"):
            input_file = os.path.join(input_path, file)
            output_file = os.path.join(output_path, file)
            trim_video(input_file, output_file, trim_end_time)


directory = "F:\\your\\videos\\path"
input_folder = os.path.join(directory, "videos")
output_folder = os.path.join(input_folder, "trimmed")
end_time = 15

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

trim_all(input_folder, output_folder, end_time)
