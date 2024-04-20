import os
from PIL import Image
import ffmpeg

def optimize_image(file_path, output_path):
    """Optimizes images and saves them to the specified output path."""
    try:
        print(f"Optimizing and copying image: {file_path}")
        image = Image.open(file_path)
        image.save(output_path, optimize=True, quality=85)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error optimizing image {file_path}: {e}")

def optimize_video(file_path, output_path):
    """Optimizes videos and saves them to the specified output path."""
    print(f"Optimizing and copying video: {file_path}")
    try:
        ffmpeg.input(file_path).output(output_path, codec='libx264', crf=28, preset='medium').run(overwrite_output=True)
        print(f"Video saved to {output_path}")
    except ffmpeg.Error as e:
        print(f"Failed to optimize video {file_path}: {e}")

def process_directory(directory):
    """Processes directories to find original media, optimize it, and copy to optimized directory."""
    print(f"Processing directory: {directory}")
    for root, dirs, files in os.walk(directory):
        print(f"Current directory: {root}")
        for file in files:
            print(f"Processing file: {file}")
            original_path = os.path.join(root, file)
            optimized_path = original_path.replace('original', 'optimized')
            if not os.path.exists(optimized_path):
                os.makedirs(os.path.dirname(optimized_path), exist_ok=True)
                if file.lower().endswith(('png', 'jpg', 'jpeg')):
                    optimize_image(original_path, optimized_path)
                elif file.lower().endswith(('mp4', 'mov')):
                    optimize_video(original_path, optimized_path)
            else:
                print(f"Optimized file already exists: {optimized_path}")

def main():
    process_directory('./global/media/original')
    process_directory('./project1/media/original')

if __name__ == '__main__':
    main()
