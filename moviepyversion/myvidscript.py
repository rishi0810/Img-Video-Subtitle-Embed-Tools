from moviepy.editor import *
import json

# ---------- SETTINGS ----------
image_path = "img.jpg"
audio_path = "story2.mp3"
json_path = "sampleScript.json"
video_duration = 101  # seconds
fps = 30
w, h = 1280, 720

# ---------- LOAD IMAGE ----------
bg = ImageClip(image_path).resize((w, h)).set_duration(video_duration)

# Optional: Add subtle zoom to background (remove if not needed)
bg = bg.fx(vfx.zoom_in, final_scale=1.05, duration=video_duration)

# ---------- LOAD AUDIO ----------
audio = AudioFileClip(audio_path).subclip(0, video_duration)

# ---------- LOAD SUBTITLE JSON ----------
with open(json_path) as f:
    subtitles = json.load(f)

# ---------- CREATE SUBTITLE CLIPS ----------
subtitle_clips = []
for sub in subtitles:
    start = sub["startFrame"] / fps
    duration = sub["durationInFrames"] / fps
    text = sub["text"]

    # Create the subtitle clip (no animation inside TextClip, just static)
    text_clip = TextClip(
        text,
        fontsize=40,
        font="Arial",  # Make sure 'Poppins' is installed
        color="white",
        method='caption',
        size=(w - 100, None)
    ).set_position(("center", h - 100)).set_duration(duration)

    # Apply fade in and out
    text_clip = text_clip.fadein(0.5).fadeout(0.5)

    # Set start time
    subtitle_clips.append(text_clip.set_start(start))

# ---------- COMBINE ----------
video = CompositeVideoClip([bg, *subtitle_clips])
video = video.set_audio(audio)

# ---------- EXPORT ----------
video.write_videofile("final_output_with_fade.mp4", fps=fps, codec='libx264', audio_codec='aac')
