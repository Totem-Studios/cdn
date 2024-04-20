import os
from PIL import Image
import ffmpeg

def optimize_image(file_path, output_path):
    print(f"Optimizing image: {file_path}")
    try:
        image = Image.open(file_path)
        image.save(output_path, optimize=True, quality=85)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error optimizing image {file_path}: {e}")

def optimize_video(file_path, output_path):
    print(f"Optimizing video: {file_path}")
    try:
        ffmpeg.input(file_path).output(output_path, codec='libx264', crf=23).run(overwrite_output=True)
        print(f"Video saved to {output_path}")
    except ffmpeg.Error as e:
        print(f"Failed to optimize video {file_path}: {e}")

def process_directory(directory):
    print(f"Processing directory: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'original' in root:
                output_root = root.replace('original', 'optimized')
                os.makedirs(output_root, exist_ok=True)
                output_path = os.path.join(output_root, file)
                if not os.path.exists(output_path):
                    if file.lower().endswith(('png', 'jpg', 'jpeg')):
                        optimize_image(file_path, output_path)
                    elif file.lower().endswith(('mp4', 'mov')):
                        optimize_video(file_path, output_path)

def main():
    process_directory('./global/media/original')
    for i in range(1, 13):  # Adjust the range based on your project numbers
        process_directory(f'./project{i}/media/original')

if __name__ == '__main__':
    main()
