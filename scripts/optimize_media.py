import os
from PIL import Image
import ffmpeg

def optimize_images(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            original_path = os.path.join(source_folder, filename)
            optimized_path = os.path.join(target_folder, filename)
            if not os.path.exists(optimized_path):
                image = Image.open(original_path)
                image.save(optimized_path, optimize=True, quality=85)

def optimize_videos(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(('.mp4', '.mov')):
            original_path = os.path.join(source_folder, filename)
            optimized_path = os.path.join(target_folder, filename)
            if not os.path.exists(optimized_path):
                stream = ffmpeg.input(original_path)
                stream = ffmpeg.output(stream, optimized_path, codec='libx264', crf=23)
                ffmpeg.run(stream)

def main():
    source_folder = './media/original'
    target_folder = './media/optimized'
    os.makedirs(target_folder, exist_ok=True)
    optimize_images(source_folder, target_folder)
    optimize_videos(source_folder, target_folder)

if __name__ == '__main__':
    main()
