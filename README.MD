## 🎬 Image to Video Converter with Subtitles and Audio

This Python project takes a **static image** and generates a **full-length video** with:
- Embedded **subtitles** (from a JSON file)
- Background **audio**
- Optional **zoom effect**
- Uses **MoviePy** and **FFmpeg**

---

### 🔧 Requirements

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to PATH
- Python packages:
  ``` bash
  pip install moviepy
  ```

## 📁 Project Structure

```
image2video/
│
├── ffmpeg_version/
│   ├── __init__.py
│   ├── add_audio.py
│   ├── image_to_video.py
│   └── json_to_srt.py
│
├── moviepy_version/
│   ├── __init__.py
│   └── generate_video.py
│
├── assets/
│   ├── your_image.jpg
│   ├── your_audio.mp3
│   └── subtitles.json
│
├── output/
│   └── final_output_with_fade.mp4
│
├── .gitignore
├── README.md
└── requirements.txt

```

---

## 📜 Subtitle JSON Format

```json
[
  {
    "text": "Hello world!",
    "startFrame": 0,
    "durationInFrames": 90
  },
  {
    "text": "Enjoy the video.",
    "startFrame": 100,
    "durationInFrames": 120
  }
]
```

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

It generates a video named `final_output_with_fade.mp4`.

---

## 💡 Features

* Subtle **zoom-in** effect on image
* Subtitles appear with **fade-in/out**
* Uses **Poppins** font (install on system if not available)
* Supports full HD (1280x720) output

---

## 📦 Output

* `final_output_with_fade.mp4` — Your final video!



