import os
from PIL import Image
import ffmpeg

def optimize_image(file_path, output_path):
    try:
        print(f"Starting image optimization: {file_path}")
        image = Image.open(file_path)
        image.save(output_path, optimize=True, quality=85)
        print(f"Image optimized and saved to: {output_path}")
    except Exception as e:
        print(f"Error optimizing image {file_path}: {e}")

def optimize_video(file_path, output_path):
    try:
        print(f"Starting video optimization: {file_path}")
        ffmpeg.input(file_path).output(output_path, codec='libx264', crf=28, preset='medium').run(overwrite_output=True)
        print(f"Video optimized and saved to: {output_path}")
    except ffmpeg.Error as e:
        print(f"Failed to optimize video {file_path}: {e}")

def process_directory(directory):
    print(f"Processing directory: {directory}")
    for root, dirs, files in os.walk(directory):
        print(f"Current directory: {root}, Files: {files}")
        for file in files:
            original_path = os.path.join(root, file)
            optimized_path = original_path.replace('original', 'optimized')
            if not os.path.exists(optimized_path):
                os.makedirs(os.path.dirname(optimized_path), exist_ok=True)
                if file.lower().endswith(('png', 'jpg', 'jpeg')):
                    optimize_image(original_path, optimized_path)
                elif file.lower().endswith(('mp4', 'mov')):
                    optimize_video(original_path, optimized_path)

def main():
    process_directory('./global/media/original')
    process_directory('./project1/media/original')

if __name__ == '__main__':
    main()
