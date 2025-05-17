import json

def frames_to_srt_time(frame, fps):
    total_seconds = frame / fps
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    s = int(total_seconds % 60)
    ms = int((total_seconds % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def json_to_srt(json_data, fps, output_file):
    with open(output_file, "w") as f:
        for i, entry in enumerate(json_data):
            start = frames_to_srt_time(entry["startFrame"], fps)
            end = frames_to_srt_time(entry["startFrame"] + entry["durationInFrames"], fps)
            text = entry["text"]
            f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

with open("sampleScript.json") as f:
    data = json.load(f)

json_to_srt(data, fps=30, output_file="subtitles.srt")
