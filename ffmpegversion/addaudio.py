import subprocess

def add_audio_to_video(video_path, audio_path, output_path):
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",  # Stops when the shortest stream ends
        output_path
    ]
    subprocess.run(cmd, check=True)

# Example usage
add_audio_to_video("final_video.mp4", "story2.mp3", "video_with_audio.mp4")
