import os
import subprocess

# Define your directories
source_directory = './global/media/original/video'
output_directory = './global/media/optimized/video'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop over all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".mp4"):
        input_path = os.path.join(source_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Construct the FFmpeg command to optimize the video
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '23',
            '-c:a', 'copy',  # Copy the audio stream without re-encoding
            output_path
        ]

        # Execute the command
        subprocess.run(cmd, check=True)

print("Video optimization complete.")
