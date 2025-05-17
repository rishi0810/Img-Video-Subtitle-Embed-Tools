from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.fx.Resize import Resize

import json

image_path = "your_image.png"
audio_path = "your_audio.mp3"
json_path = "your_script_json.json"
video_duration = 101  # seconds
fps = 25
w, h = 720, 1280

bg = ImageClip(image_path).resized(width=w, height=h).with_duration(video_duration)


bg = bg.with_effects([Resize(lambda t: 1 + (0.05 * t / video_duration))])


audio = AudioFileClip(audio_path).subclipped(0, video_duration)


with open(json_path) as f:
    subtitles = json.load(f)


subtitle_clips = []
for sub in subtitles:
    start = sub["startFrame"] / fps
    duration = sub["durationInFrames"] / fps
    text = sub["text"]


    text_clip = TextClip(
        color="white",
        font="Arial",
        text=text,
        font_size=40,  
        stroke_color="white",
        stroke_width=1,
    ).with_position(("center", h - 100)).with_duration(duration)

    subtitle_clips.append(text_clip.with_start(start))

video = CompositeVideoClip([bg] + subtitle_clips)   
video = video.with_audio(audio)

video.write_videofile("final_output_with_fade.mp4", fps=fps, codec='libx264', audio_codec='aac')

print("Video processing complete: final_output_with_fade.mp4")