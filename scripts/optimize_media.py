import os
import subprocess

def optimize_video(input_path, output_path):
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Construct the FFmpeg command for optimizing the video
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'libx264',  # Video codec
        '-preset', 'fast',  # Preset for encoding speed vs compression rate
        '-crf', '23',       # Constant Rate Factor for quality level
        '-c:a', 'aac',      # Audio codec
        '-b:a', '160k',     # Audio bitrate
        output_path
    ]
    
    # Execute the command
    subprocess.run(cmd, check=True)

def process_directory(directory, output_root):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.mp4'):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, directory)
                output_directory = os.path.join(output_root, relative_path)
                output_path = os.path.join(output_directory, filename)
                optimize_video(input_path, output_path)

# Example usage
source_directory = './global/media/original'
output_directory = './global/media/optimized'
process_directory(source_directory, output_directory)

print("Video optimization complete.")
