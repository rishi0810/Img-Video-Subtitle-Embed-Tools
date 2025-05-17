import cv2

def image_to_video_opencv(image_path, output_path, duration_sec, fps=30):
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    total_frames = int(duration_sec * fps)
    for _ in range(total_frames):
        out.write(img)

    out.release()

image_to_video_opencv("img.jpg", "output.mp4", duration_sec=101, fps=30)
