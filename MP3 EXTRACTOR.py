import os
from moviepy.editor import *

def video_to_sound(video_path):
    name = os.path.basename(video_path)
    song_path = os.path.dirname(video_path)
    name = os.path.splitext(name)[0]
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(os.path.join(f"{song_path}/{name}.mp3"), codec='mp3')

if __name__ == "__main__":
    print("Drag 'n Drop Video Here:")
    movie_path = input(" >> ").strip('"')
    video_to_sound(movie_path)
